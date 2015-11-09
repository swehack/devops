# hlreporter - HP RAID collector for www.monitorscout.com
# by Stefan Midjich <swehack@gmail.com>
#
# Depends on the hpacucli tool from HP Linux repos.
# Change hpacucli_path to path for hpssacli if relevant, syntax and output
# are the same.
#

import os
import subprocess

from hlreporterlib import collector
from hlreporterlib import errors

hpacucli_path = '/usr/sbin/hpacucli'


class HPRAIDCollector(collector.BaseCollector):
    name = 'HP RAID collector'
    platforms = ['linux']

    def _parseOutput(data):
        controllers = []

        controller = {}
        for line in data.split('\n'):
            if not len(line):
                continue

            if not line.startswith(' '):
                if len(controller.keys()):
                    controllers.append(controller)
                controller = {}
                controller_name = line.strip(' ')
                controller[controller_name] = {}
            else:
                if controller_name is None:
                    continue
                (component, status) = line.strip(' ').split(': ')
                controller[controller_name][component] = status
        else:
            controllers.append(controller)

        return controllers

    def collect(self):
        self.root = self.device.initComponentGroup('hardware')
        hp = self.root.initComponentGroup('hp')
        raid = hp.initComponent('raid')

        # Get RAID controllers
        controllers = getRAIDControllers()
        if not len(controllers):
            return

        for controller in controllers:
            controller_name = controller.keys()[0]
            for (
                component_name,
                component_status
            ) in controller[controller_name].iteritems():
                if component_status == 'OK':
                    status = True
                else:
                    status = False
                metric = raid.initMetric(
                    '{name}: {component}'.format(
                        name=controller_name,
                        component=component_name
                    ),
                    status,
                    'BOOLEAN',
                    'status'
                )

    def getRAIDControllers(self):
        command = '{0} controller all show status'.format(hpacucli_path)
        (stdout, stderr) = subprocess.Popen(
            command.split(' '),
            stdout=subprocess.PIPE
        )
        return self._parseOutput(output)

    def canCollect(self):
        return os.path.isfile(hpacucli_path) and \
                os.access(hpacucli_path, (os.X_OK & os.R_OK))
