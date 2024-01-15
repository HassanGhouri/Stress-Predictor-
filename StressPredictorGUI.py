import tkinter as tk
from tkinter import ttk
import numpy as np
import stressModel


class StressPredictorGUI:
    """
    A graphical user interface for predicting stress levels based on user input.

    Attributes:
    root (Tk):
        The main Tkinter window for the GUI.
    ct:
        A container for preprocessing data.
    model:
        The stress prediction model.

    Methods:
    __init__(self, root, ct, model):
        Initializes the GUI with input fields and buttons.
    predict_stress(self):
        Predicts stress levels based on user input and displays the result.

    Example Usage:
    gui = StressPredictorGUI(root, container, stress_model)
    root.mainloop()
    """

    def __init__(self, root, ct, model):
        self.root = root
        self.root.title("Stress Level Predictor")
        self.ct = ct
        self.model = model

        # Create input fields
        self.gender_label = ttk.Label(root, text="Gender:")
        self.gender_values = ["Male", "Female"]
        self.gender_combobox = ttk.Combobox(root, values=self.gender_values)

        self.age_label = ttk.Label(root, text="Age:")
        self.age_entry = ttk.Entry(root)

        self.sleep_duration_label = ttk.Label(root, text="Sleep Duration (hours):")
        self.sleep_duration_entry = ttk.Entry(root)

        self.sleep_quality_label = ttk.Label(root, text="Sleep Quality (1-10):")
        self.sleep_quality_entry = ttk.Entry(root)

        self.physical_activity_label = ttk.Label(root, text="Physical Activity Level(1-100):")
        self.physical_activity_entry = ttk.Entry(root)

        self.bmi_category_label = ttk.Label(root, text="BMI Category:")
        self.bmi_values = ["Normal", "Overweight", "Obese", "Underweight"]
        self.bmi_combobox = ttk.Combobox(root, values=self.bmi_values)

        self.bp_label = ttk.Label(root, text="Blood Pressure (Systolic/Diastolic):")
        self.bp_entry = ttk.Entry(root)

        self.heart_rate_label = ttk.Label(root, text="Heart Rate (bpm):")
        self.heart_rate_entry = ttk.Entry(root)

        self.daily_steps_label = ttk.Label(root, text="Daily Steps:")
        self.daily_steps_entry = ttk.Entry(root)

        self.sleep_disorder_label = ttk.Label(root, text="Sleep Disorder:")
        self.sleep_disorder_values = ["None", "Sleep Apnea", "Insomnia"]
        self.sleep_disorder_combobox = ttk.Combobox(root, values=self.sleep_disorder_values)

        self.submit_button = ttk.Button(root, text="Predict Stress Level", command=self.predict_stress)

        # Place input fields on the grid
        self.gender_label.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self.gender_combobox.grid(row=0, column=1, padx=5, pady=5)

        self.age_label.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)

        self.sleep_duration_label.grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)
        self.sleep_duration_entry.grid(row=2, column=1, padx=5, pady=5)

        self.sleep_quality_label.grid(row=3, column=0, sticky=tk.E, padx=5, pady=5)
        self.sleep_quality_entry.grid(row=3, column=1, padx=5, pady=5)

        self.physical_activity_label.grid(row=4, column=0, sticky=tk.E, padx=5, pady=5)
        self.physical_activity_entry.grid(row=4, column=1, padx=5, pady=5)

        self.bmi_category_label.grid(row=5, column=0, sticky=tk.E, padx=5, pady=5)
        self.bmi_combobox.grid(row=5, column=1, padx=5, pady=5)

        self.bp_label.grid(row=6, column=0, sticky=tk.E, padx=5, pady=5)
        self.bp_entry.grid(row=6, column=1, padx=5, pady=5)

        self.heart_rate_label.grid(row=7, column=0, sticky=tk.E, padx=5, pady=5)
        self.heart_rate_entry.grid(row=7, column=1, padx=5, pady=5)

        self.daily_steps_label.grid(row=8, column=0, sticky=tk.E, padx=5, pady=5)
        self.daily_steps_entry.grid(row=8, column=1, padx=5, pady=5)

        self.sleep_disorder_label.grid(row=9, column=0, sticky=tk.E, padx=5, pady=5)
        self.sleep_disorder_combobox.grid(row=9, column=1, padx=5, pady=5)

        self.submit_button.grid(row=10, column=0, columnspan=2, pady=10)

    def predict_stress(self):
        """
        Function to predict stress
        :return: None
        """
        input_data = [
            self.gender_combobox.get(),
            int(self.age_entry.get()),
            float(self.sleep_duration_entry.get()),
            int(self.sleep_quality_entry.get()),
            int(self.physical_activity_entry.get()),
            self.bmi_combobox.get(),
            self.bp_entry.get(),
            int(self.heart_rate_entry.get()),
            int(self.daily_steps_entry.get()),
            self.sleep_disorder_combobox.get()
        ]

        input_data = np.array(input_data, dtype=object)
        input_data = stressModel.prepData([input_data], self.ct)
        stress_level = self.model.predict(input_data)

        result_label = ttk.Label(self.root, text=f"Predicted Stress Level: {stress_level[0]:.2f}")

        result_label.grid(row=11, column=0, columnspan=2, pady=10)


# Initialize the GUI
model, ct = stressModel.modelMaker()
root = tk.Tk()
app = StressPredictorGUI(root, ct, model)
root.mainloop()
