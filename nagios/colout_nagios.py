# Solarized colout theme for nagios logs
#  * Install colout from https://github.com/nojhan/colout
#  * mkdir ~/.colout
#  * Install this file into ~/.colout/colout_nagios.py
#  * tail -0f /var/log/nagios3/nagios.log | perl -pi -e 's/(\d+)/localtime($1)/e' | colout -T ~/.colout -t nagios
#
# By Stefan Midjich

def theme():
    # Solarized specific colors: http://ethanschoonover.com/solarized
    bright_red = '#d75f00'
    red = '#dc322f'
    yellow = '#b58900'
    green = '#859900'
    bright_white = '#ffffd7'
    white = '#e4e4e4'
    cyan = '#2aa198'
    bright_black = '#1c1c1c'
    orange = '#cb4b16'

    return [
        [ "(SERVICE ALERT\:) (.+)(;OK;HARD;)(.+)$", green ],
        [ "(SERVICE ALERT\:) (.+)(;OK;SOFT;)(.+)$", "#2aa198" ],
        [ "(SERVICE ALERT\:) (.+;)(UNKNOWN|CRITICAL)(;HARD;)(.+)$", bright_red ],
        [ "(SERVICE ALERT\:) (.+;)(UNKNOWN|CRITICAL)(;SOFT;)(.+)$", yellow ],
        [ "(SERVICE ALERT\:) (.+)(;WARNING;HARD;)(.+)$", red ],
        [ "(SERVICE ALERT\:) (.+)(;WARNING;SOFT;)(.+)$", yellow ],
        [ "(HOST ALERT\:) (.+)(;UP;HARD;)(.+)$", green ],
        [ "(HOST ALERT\:) (.+)(;UP;SOFT;)(.+)$", cyan ],
        [ "(HOST ALERT\:) (.+)(;DOWN;HARD;)(.+)$", bright_red ],
        [ "(HOST ALERT\:) (.+)(;DOWN;SOFT;)(.+)$", yellow ],
        [ "(EXTERNAL COMMAND\:) (.+)$", white, "bold" ],
        [ "(Finished daemonizing.+)$", bright_white ],
        [ "(Successfully shutdown.+)$", orange ],
    ]
