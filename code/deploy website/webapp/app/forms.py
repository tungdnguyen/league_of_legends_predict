from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class TeamForm(FlaskForm):
	blueplayer1=StringField('Blue Player 1', validators=[DataRequired()])
	bluechamp1=StringField('Blue Champion 1', validators=[DataRequired()])
	blueplayer2=StringField('Blue Player 2', validators=[DataRequired()])
	bluechamp2=StringField('Blue Champion 2', validators=[DataRequired()])
	blueplayer3=StringField('Blue Player 3', validators=[DataRequired()])
	bluechamp3=StringField('Blue Champion 3', validators=[DataRequired()])
	blueplayer4=StringField('Blue Player 4', validators=[DataRequired()])
	bluechamp4=StringField('Blue Champion 4', validators=[DataRequired()])
	blueplayer5=StringField('Blue Player 5', validators=[DataRequired()])
	bluechamp5=StringField('Blue Champion 5', validators=[DataRequired()])
	
	bluerole1=SelectField('Blue Role 1', validators=[DataRequired()], choices=[('TOP','TOP'), ('JUNGLE','JUNGLE'), ('MIDDLE','MIDDLE'), ('CARRY','CARRY'), ('SUPPORT','SUPPORT')])
	bluerole2=SelectField('Blue Role 2', validators=[DataRequired()], choices=[('TOP','TOP'), ('JUNGLE','JUNGLE'), ('MIDDLE','MIDDLE'), ('CARRY','CARRY'), ('SUPPORT','SUPPORT')])
	bluerole3=SelectField('Blue Role 3', validators=[DataRequired()], choices=[('TOP','TOP'), ('JUNGLE','JUNGLE'), ('MIDDLE','MIDDLE'), ('CARRY','CARRY'), ('SUPPORT','SUPPORT')])
	bluerole4=SelectField('Blue Role 4', validators=[DataRequired()], choices=[('TOP','TOP'), ('JUNGLE','JUNGLE'), ('MIDDLE','MIDDLE'), ('CARRY','CARRY'), ('SUPPORT','SUPPORT')])
	bluerole5=SelectField('Blue Role 5', validators=[DataRequired()], choices=[('TOP','TOP'), ('JUNGLE','JUNGLE'), ('MIDDLE','MIDDLE'), ('CARRY','CARRY'), ('SUPPORT','SUPPORT')])
	
	redplayer1=StringField('Red Player 1', validators=[DataRequired()])
	redplayer2=StringField('Red Player 2', validators=[DataRequired()])
	redplayer3=StringField('Red Player 3', validators=[DataRequired()])
	redplayer4=StringField('Red Player 4', validators=[DataRequired()])
	redplayer5=StringField('Red Player 5', validators=[DataRequired()])
	
	redchamp1=StringField('Red Champ 1', validators=[DataRequired()])
	redchamp2=StringField('Red Champ 2', validators=[DataRequired()])
	redchamp3=StringField('Red Champ 3', validators=[DataRequired()])
	redchamp4=StringField('Red Champ 4', validators=[DataRequired()])
	redchamp5=StringField('Red Champ 5', validators=[DataRequired()])
	
	redrole1=SelectField('Red Role 1', validators=[DataRequired()], choices=[('TOP','TOP'), ('JUNGLE','JUNGLE'), ('MIDDLE','MIDDLE'), ('CARRY','CARRY'), ('SUPPORT','SUPPORT')])
	redrole2=SelectField('Red Role 2', validators=[DataRequired()], choices=[('TOP','TOP'), ('JUNGLE','JUNGLE'), ('MIDDLE','MIDDLE'), ('CARRY','CARRY'), ('SUPPORT','SUPPORT')])
	redrole3=SelectField('Red Role 3', validators=[DataRequired()], choices=[('TOP','TOP'), ('JUNGLE','JUNGLE'), ('MIDDLE','MIDDLE'), ('CARRY','CARRY'), ('SUPPORT','SUPPORT')])
	redrole4=SelectField('Red Role 4', validators=[DataRequired()], choices=[('TOP','TOP'), ('JUNGLE','JUNGLE'), ('MIDDLE','MIDDLE'), ('CARRY','CARRY'), ('SUPPORT','SUPPORT')])
	redrole5=SelectField('Red Role 5', validators=[DataRequired()], choices=[('TOP','TOP'), ('JUNGLE','JUNGLE'), ('MIDDLE','MIDDLE'), ('CARRY','CARRY'), ('SUPPORT','SUPPORT')])
	
	
	
	submit=SubmitField('Predict')