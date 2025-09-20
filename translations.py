translations = {
    "en_US": {
        "Select DB File": "Select DB File",
        "Browse File": "Browse File",
        "Select Target Folder": "Select Target Folder",
        "Browse Folder": "Browse Folder",
        "Move File": "Move File",
        "File selected": "File selected",
        "Folder selected": "Folder selected",
        "Please select file and folder": "Please select file and folder",
        "File moved successfully": "File moved successfully",
        "Error moving file": "Error moving file",
        "Default Target Folder": "Default Target Folder",
        "Select Language": "Select Language",
        "Save": "Save",
        "Settings saved. Restart app for full effect.": "Settings saved. Restart app for full effect."
    },
    "fr_FR": {
        "Select DB File": "Sélectionner le fichier DB",
        "Browse File": "Parcourir le fichier",
        "Select Target Folder": "Sélectionner le dossier cible",
        "Browse Folder": "Parcourir le dossier",
        "Move File": "Déplacer le fichier",
        "File selected": "Fichier sélectionné",
        "Folder selected": "Dossier sélectionné",
        "Please select file and folder": "Veuillez sélectionner un fichier et un dossier",
        "File moved successfully": "Fichier déplacé avec succès",
        "Error moving file": "Erreur lors du déplacement du fichier",
        "Default Target Folder": "Dossier cible par défaut",
        "Select Language": "Sélectionner la langue",
        "Save": "Enregistrer",
        "Settings saved. Restart app for full effect.": "Paramètres enregistrés. Redémarrez l'application pour un effet complet."
    },
    "de_DE": {
        "Select DB File": "DB-Datei auswählen",
        "Browse File": "Datei durchsuchen",
        "Select Target Folder": "Zielordner auswählen",
        "Browse Folder": "Ordner durchsuchen",
        "Move File": "Datei verschieben",
        "File selected": "Datei ausgewählt",
        "Folder selected": "Ordner ausgewählt",
        "Please select file and folder": "Bitte wählen Sie eine Datei und einen Ordner aus",
        "File moved successfully": "Datei erfolgreich verschoben",
        "Error moving file": "Fehler beim Verschieben der Datei",
        "Default Target Folder": "Standard-Zielordner",
        "Select Language": "Sprache auswählen",
        "Save": "Speichern",
        "Settings saved. Restart app for full effect.": "Einstellungen gespeichert. Starten Sie die App neu für volle Wirkung."
    }
}

def get_translation(text, language):
    return translations.get(language, translations["en_US"]).get(text, text)