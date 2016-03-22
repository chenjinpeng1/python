#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import fram

class MyHandler(fram.BaseHandler):

    def execute(self):
        print ('event-drive execute MyHandler')


fram.event_list.append(MyHandler) # 注册事件
fram.run()