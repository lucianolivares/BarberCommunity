# The model implements the observer pattern. This means that the class must
# support adding, removing, and alerting observers. In this case, the model is
# completely independent of controllers and views. It is important that all
# registered observers implement a specific method that will be called by the
# model when they are notified (in this case, it is the `model_is_changed`
# method). For this, observers must be descendants of an abstract class,
# inheriting which, the `model_is_changed` method must be overridden.
import multitasking


multitasking.set_max_threads(10)

class MainScreenModel:
    def __init__(self, base):
        self.base = base

        self.barbers = dict()
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
    def check_data(self):
        """
        Get data from the database and compares this data with the data entered
        by the user.
        This method is completely asynchronous. It does not return any value.
        """
        data = self.base.get_barbers_data()
        self.get_data_status = False
        barbers = dict()

        for barber in data:
            id = barber.id
            barber = barber.to_dict()
            barbers[id] = barber

        self.barbers = barbers
        self.get_data_status = True

    
    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.model_is_changed()
