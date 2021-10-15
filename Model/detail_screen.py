import multitasking

class DetailScreenModel:
    def __init__(self, base):
        self.base = base
        self.barber = dict()
        self._get_data_status = None
        self._observers = []
        
    @property
    def get_data_status(self):
        return self._get_data_status

    @get_data_status.setter
    def get_data_status(self, value):
        self._get_data_status = value
        # We notify the View -
        # :class:`~View.MainScreen.main_screen.MainScreenView` about the
        # changes that have occurred in the data model.
        self.notify_observers()

    @multitasking.task
    def get_barber(self, id):
        self.get_data_status = False
        data = self.base.get_barber(id)
        self.barber = data
        self.get_data_status = True

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.model_is_changed()
