#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import traceback

from tcex import TcEx

tcex = TcEx()
args = tcex.args


def main():
    tcex.log.info('Doing stuff in {}'.format(args.api_default_org))
    resource = tcex.resources.Indicator(tcex)
    resource.owner = args.api_default_org
    resource.url = args.tc_api_path

    for results in resource:  # pagination
        if results.get('status') == 'Success':
            print(json.dumps(results.get('data', []), indent=4))
        else:
            warn = 'Failed retrieving result during pagination.'
            tcex.log.error(warn)


if __name__ == "__main__":
    try:
        # start the app
        main()
    except SystemExit:
        pass
    except Exception as e:  # if there are any strange errors, log it to the logging in the UI
        err = 'Generic Error.  See logs for more details ({}).'.format(e)
        tcex.log.error(traceback.format_exc())
        tcex.message_tc(err)
        tcex.playbook.exit(1)
