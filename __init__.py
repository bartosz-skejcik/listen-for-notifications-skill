from mycroft import MycroftSkill, intent_file_handler


class ListenForNotifications(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('notifications.for.listen.intent')
    def handle_notifications_for_listen(self, message):
        app_name = ''
        body = ''
        title = ''

        self.speak_dialog('notifications.for.listen', data={
            'body': body,
            'app_name': app_name,
            'title': title
        })


def create_skill():
    return ListenForNotifications()

