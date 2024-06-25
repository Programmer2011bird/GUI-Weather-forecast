import customtkinter as ctk
import FetchWeather

# Setting the appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class Application(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Configs
        self.geometry("520x350")
        self.resizable(False, False)
        self.wm_title("Weather Forcast")

        self.ENTRY_PLACE: ctk.CTkEntry = ctk.CTkEntry(self, placeholder_text="Enter City Name", width=300)
        self.BUTTON_SEARCH: ctk.CTkButton = ctk.CTkButton(self, text="Search", command=self.Show_Weather)

        self.ENTRY_PLACE.grid(row=0, column=0, padx=17, pady=10)
        self.BUTTON_SEARCH.grid(row=0, column=1, padx=10, pady=10)

    def Show_Weather(self):
        # Getting the user input and then getting the data from API and passing the user input into it
        PLACE: str = str(self.ENTRY_PLACE.get())
        INFO: dict = FetchWeather.Fetch_Weather(place=PLACE)
        # Showing the outputs and all the information
        LABEL_DATE = ctk.CTkLabel(self, text=f"Date : {INFO['DateAndTime']}", font=(ctk.CTkFont("monospace", 20)))
        LABEL_TEMPERATURE = ctk.CTkLabel(self, text=f"Temperature : {INFO['Temperature']}",
                                         font=(ctk.CTkFont("monospace", 20)))
        LABEL_HUMIDITY = ctk.CTkLabel(self, text=f"Humidity : {INFO['Humidity']}", font=(ctk.CTkFont("monospace", 20)))
        LABEL_SUNRISE = ctk.CTkLabel(self, text=f"Sunrise : {INFO['Sunrise']}", font=(ctk.CTkFont("monospace", 20)))
        LABEL_SUNSET = ctk.CTkLabel(self, text=f"Sunset : {INFO['Sunset']}", font=(ctk.CTkFont("monospace", 20)))
        LABEL_Conditions = ctk.CTkLabel(self, text=f"Condition : {INFO['Conditions']}",
                                        font=(ctk.CTkFont("monospace", 20)))

        LABEL_DATE.grid(row=1, column=0, pady=5, padx=20)
        LABEL_TEMPERATURE.grid(row=2, column=0, pady=5, padx=20)
        LABEL_HUMIDITY.grid(row=3, column=0, pady=5, padx=20)
        LABEL_SUNRISE.grid(row=4, column=0, pady=5, padx=20)
        LABEL_SUNSET.grid(row=5, column=0, pady=5, padx=20)
        LABEL_Conditions.grid(row=6, column=0, pady=5, padx=20)


# Running the program
if __name__ == "__main__":
    App = Application()
    App.mainloop()
