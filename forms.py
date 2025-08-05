from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField,  StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from wtforms.fields import EmailField
from flask_wtf.file import FileField, FileAllowed
from wtforms import ValidationError


class ConnexionForm(FlaskForm):
    email = EmailField("Adresse email", validators=[DataRequired(), Email(message="Adresse email invalide"), Length(max=150)])
    mot_de_passe = PasswordField("Mot de passe", validators=[DataRequired(), Length(min=6, max=200)])
    submit = SubmitField("Se connecter")


class InscriptionForm(FlaskForm):
    email = EmailField("Adresse email", validators=[
        DataRequired(),
        Email(message="Adresse email invalide"),
        Length(max=150)
    ])

    mot_de_passe = PasswordField("Mot de passe", validators=[
        DataRequired(),
        Length(min=6, max=200)
    ])

    username = StringField("Nom d'utilisateur", validators=[
        DataRequired(),
        Length(min=3, max=80)
    ])

    submit = SubmitField("S'inscrire")


class IdeeForm(FlaskForm):
    titre = StringField("Titre", validators=[DataRequired(), Length(min=3, max=100)])

    def pas_vide_apres_strip(form, field):
        if not field.data or not field.data.strip():
            raise ValidationError("Le contenu ne peut pas être vide ou fait uniquement d'espaces.")

    contenu = TextAreaField("Contenu", validators=[
        DataRequired(),
        pas_vide_apres_strip,
        Length(min=10, max=1000, message="Le contenu doit faire entre 10 et 1000 caractères.")
    ])

    submit = SubmitField("Soumettre l'idée")


class CommentaireForm(FlaskForm):
    def pas_vide_apres_strip(form, field):
        if not field.data or not field.data.strip():
            raise ValidationError("Le commentaire ne peut pas être vide ou fait uniquement d'espaces.")

    contenu = TextAreaField("Commentaire", validators=[
        DataRequired(),
        pas_vide_apres_strip,
        Length(min=5, max=500, message="Le commentaire doit faire entre 5 et 500 caractères.")
    ])

    submit = SubmitField("Commenter")


class EditProfileForm(FlaskForm):
    bio = TextAreaField("Biographie", validators=[DataRequired(), Length(max=500)])
    centres_interet = TextAreaField("Centres d'intérêt", validators=[DataRequired(), Length(max=300)])
    photo = FileField("Photo de profil", validators=[FileAllowed(['jpg', 'jpeg', 'png'], "Images uniquement !")])
    submit = SubmitField("Soumettre")
    nom_affiche = StringField("Nom affiché", validators=[
        DataRequired(),
        Length(min=3, max=80)
    ])

