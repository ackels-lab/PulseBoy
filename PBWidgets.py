from PyQt5 import QtWidgets
import simpleValveDesign
import noiseValveDesign
import trialDesign


# TODO - These widgets could inherit from a common PBWidget parent that implements remove_from_parent etc.
class SimpleValveWidget(QtWidgets.QWidget, simpleValveDesign.Ui_Form):
    def __init__(self, parentUi=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.parentUi = parentUi

        self.removeButton.clicked.connect(self.remove_from_parent)

    def remove_from_parent(self):
        self.parentUi.layout().removeWidget(self)
        self.deleteLater()

    def get_parameters(self):
        params = dict()

        params['type'] = 'Simple'

        params['fromValues'] = bool(self.fromValuesRadio.isChecked())
        params['fromDuty'] = bool(self.fromDutyRadio.isChecked())
        params['isClean'] = bool(self.cleanRadio.isChecked())
        params['isShatter'] = bool(self.shatterRadio.isChecked())
        params['fromRepeats'] = bool(self.repeatsRadio.isChecked())
        params['fromLength'] = bool(self.lengthRadio.isChecked())

        params['onset'] = float(self.onsetEdit.text())
        params['offset'] = float(self.offsetEdit.text())
        params['pulse_width'] = float(self.pulseWidthEdit.text())
        params['pulse_delay'] = float(self.pulseDelayEdit.text())
        params['frequency'] = float(self.frequencyEdit.text())
        params['duty'] = float(self.pulseDutyEdit.text()) * 0.01
        params['shatter_frequency'] = float(self.shatterHzEdit.text())
        params['shatter_duty'] = float(self.shatterDutyEdit.text()) * 0.01
        params['repeats'] = int(self.repeatsEdit.text())
        params['length'] = float(self.lengthEdit.text())

        return params

    def set_parameters(self, params):

        self.fromValuesRadio.setChecked(params['fromValues'])
        self.fromDutyRadio.setChecked(params['fromDuty'])
        self.cleanRadio.setChecked(params['isClean'])
        self.shatterRadio.setChecked(params['isShatter'])
        self.repeatsRadio.setChecked(params['fromRepeats'])
        self.lengthRadio.setChecked(params['fromLength'])

        self.onsetEdit.setText(str(params['onset']))
        self.offsetEdit.setText(str(params['offset']))
        self.pulseWidthEdit.setText(str(params['pulse_width']))
        self.pulseDelayEdit.setText(str(params['pulse_delay']))
        self.frequencyEdit.setText(str(params['frequency']))
        self.pulseDutyEdit.setText(str(params['duty']))
        self.shatterHzEdit.setText(str(params['shatter_frequency']))
        self.shatterDutyEdit.setText(str(params['shatter_duty']))
        self.repeatsEdit.setText(str(params['repeats']))
        self.lengthEdit.setText(str(params['length']))


class NoiseValveWidget(QtWidgets.QWidget, noiseValveDesign.Ui_Form):
    def __init__(self, parentUi=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.parentUi = parentUi

        self.removeButton.clicked.connect(self.remove_from_parent)

    def remove_from_parent(self):
        self.parentUi.layout().removeWidget(self)
        self.deleteLater()

    def get_parameters(self):
        params = dict()

        params['type'] = 'Noise'

        params['fromRepeats'] = bool(self.repeatsRadio.isChecked())
        params['fromLength'] = bool(self.lengthRadio.isChecked())

        params['onset'] = float(self.onsetEdit.text())
        params['offset'] = float(self.offsetEdit.text())
        params['frequency'] = float(self.frequencyEdit.text())
        params['seed'] = float(self.seedEdit.text())
        params['amp_min'] = float(self.ampMinEdit.text()) * 0.01
        params['amp_max'] = float(self.ampMaxEdit.text()) * 0.01
        params['repeats'] = int(self.repeatsEdit.text())
        params['length'] = float(self.lengthEdit.text())

        return params

    def set_parameters(self, params):
        self.repeatsRadio.setChecked(params['fromRepeats'])
        self.lengthRadio.setChecked(params['fromLength'])

        self.onsetEdit.setText(str(params['onset']))
        self.offsetEdit.setText(str(params['offset']))
        self.frequencyEdit.setText(str(params['frequency']))
        self.seedEdit.setText(str(params['seed']))
        self.ampMinEdit.setText(str(params['amp_min']))
        self.ampMaxEdit.setText(str(params['amp_max']))
        self.repeatsEdit.setText(str(params['repeats']))
        self.lengthEdit.setText(str(params['length']))


class TrialWidget(QtWidgets.QWidget, trialDesign.Ui_Form):
    def __init__(self, n_valves, parent=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.parent = parent

        self.removeButton.clicked.connect(self.remove_from_parent)

        self.activeValvesEdit.setText(str(n_valves))

    def remove_from_parent(self):
        self.parent.layout().removeWidget(self)
        self.close()
