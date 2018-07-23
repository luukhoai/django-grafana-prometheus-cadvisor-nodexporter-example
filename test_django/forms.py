from accounts.forms import UserMultiModelForm


class MainForm(UserMultiModelForm):

    def __init__(self, *args, **kwargs):
        super(MainForm, self).__init__(*args, **kwargs)
