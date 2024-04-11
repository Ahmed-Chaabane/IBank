import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image


class Application:
    TEXTES_BOUTONS = [
        ("Gestion des Clients", 10),
        ("Gestion des Comptes", 220),
        ("Gestion des Opérations", 431),
        ("Événements", 642),
        ("Quitter", 853)
    ]

    def __init__(self, root):
        self.frame = None
        self.logo_photo = None
        self.bg_panel = None
        self.bg_frame = None
        self.root = root
        self.setup_fenetre()
        self.creer_frame()
        self.lier_evenement_redimensionnement()

    def setup_fenetre(self):
        self.root.geometry('1150x718')
        self.root.resizable(True, True)
        self.root.state('zoomed')
        self.root.title('Menu ibank')

    def creer_frame(self):
        self.frame = tk.Frame(self.root, bg='#fbfbfd', highlightbackground="#223f93", highlightthickness=1)
        self.frame.place(x=0, y=0, relheight=1, relwidth=0.2)

        frame_conteneur = tk.Frame(self.frame, bg='#fbfbfd')
        frame_conteneur.place(relx=0, rely=0, relwidth=1, relheight=1)

        frame_droite = tk.Frame(self.root, bg='#dedede')
        frame_droite.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        self.frame_droite = frame_droite

        self.charger_image_arriere_plan_gauche(frame_conteneur)

        logo_image = Image.open("images\\ibank.png")
        logo_image = logo_image.resize((360, 90))
        logo_photo = ImageTk.PhotoImage(logo_image)
        logo_label = tk.Label(frame_conteneur, image=logo_photo, bg='#fbfbfd')
        logo_label.pack(padx=10, pady=50)

        self.logo_photo = logo_photo

        for texte, position_y in self.TEXTES_BOUTONS:
            if texte == "Quitter":
                bouton = tk.Button(
                    frame_conteneur,
                    text=texte,
                    width=20,
                    height=1,
                    command=self.quitter_application,
                    bg='#9d052b',
                    fg='#ffffff',
                    font=('Arial', 18, 'bold'),
                    relief='raised'
                )
            else:
                bouton = tk.Button(
                    frame_conteneur,
                    text=texte,
                    width=20,
                    height=1,
                    command=lambda t=texte: self.afficher_frame(t),
                    bg='#0078bd',
                    fg='#ffffff',
                    font=('organetto bold', 18, 'bold'),
                    relief='raised'
                )
            bouton.pack(fill="both", expand=True, padx=15, pady=30)

    def charger_image_arriere_plan_gauche(self, frame_conteneur):
        try:
            self.bg_frame = Image.open("images/background.png")
            # Rotate the image to display in portrait mode
            self.bg_frame = self.bg_frame.transpose(Image.ROTATE_90)
            photo = ImageTk.PhotoImage(self.bg_frame)
            bg_label = tk.Label(frame_conteneur, image=photo)
            bg_label.image = photo
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except FileNotFoundError:
            raise Exception("Image d'arrière-plan introuvable.")

    def lier_evenement_redimensionnement(self):
        self.root.bind('<Configure>', self.mettre_a_jour_taille_frame)

    def mettre_a_jour_taille_frame(self, event):
        largeur_frame = int(self.root.winfo_width() * 0.2)
        hauteur_frame = self.root.winfo_height()
        self.frame.config(width=largeur_frame, height=hauteur_frame)

    def afficher_frame(self, texte):

        for widget in self.frame_droite.winfo_children():
            widget.destroy()

        title_label = tk.Label(self.frame_droite, text=texte, font=('organetto bold', 34), bg='#dedede')
        title_label.pack(padx=50, pady=50)

        if texte == "Gestion des Clients":

            search_frame = tk.Frame(self.frame_droite, bg='#dedede')
            search_frame.pack(padx=50, pady=50)

            text_zone = tk.Entry(search_frame, font=('Arial', 14))
            text_zone.pack(side="left")

            search_button = tk.Button(
                search_frame,
                text="Rechercher",
                width=10,
                height=1,
                command=lambda: self.rechercher_client(text_zone.get()),
                bg='#0078bd',
                fg='#ffffff',
                font=('Arial', 14, 'bold'),
                relief='raised'
            )
            search_button.pack(side="left", padx=(10, 0))

            labels_frame = tk.Frame(self.frame_droite, bg='#dedede')
            labels_frame.pack(padx=50, pady=10)

            labels = [
                "NOM CLIENT", "PRENOM CLIENT","PRENOM CLIENT", "NAI_CLI", "ADRESSE CLIENT",
                "EMAIL CLIENT", "TELEPHONE CLIENT", "CIV_CLI", "DAT_NAI_CLI", "LIE_NAI_CLI",
                "IDE_CLI", "DAT_IDE_CLI", "LIE_IDE_CLI", "SEXE", "COM_CLI"
            ]

            for i in range(15):
                if i % 3 == 0:
                    row_frame = tk.Frame(labels_frame, bg='#dedede')
                    row_frame.pack(padx=10, pady=5)

                label = tk.Label(row_frame, text=labels[i], font=('Arial', 14), bg='#dedede')
                label.pack(side="left", padx=10, pady=5)

                text_zone = tk.Entry(row_frame, font=('Arial', 14))
                text_zone.pack(side="left", padx=10, pady=5)

        elif texte == "Gestion des Comptes":

            search_frame = tk.Frame(self.frame_droite, bg='#dedede')
            search_frame.pack(padx=50, pady=50)

            text_zone = tk.Entry(search_frame, font=('Arial', 14))
            text_zone.pack(side="left")

            search_button = tk.Button(
                search_frame,
                text="Rechercher",
                width=10,
                height=1,
                command=lambda: self.rechercher_client(text_zone.get()),
                bg='#0078bd',
                fg='#ffffff',
                font=('Arial', 14, 'bold'),
                relief='raised'
            )
            search_button.pack(side="left", padx=(10, 0))

    def quitter_application(self):
        if messagebox.askokcancel("Quitter", "Êtes-vous sûr de vouloir quitter?"):
            self.root.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()