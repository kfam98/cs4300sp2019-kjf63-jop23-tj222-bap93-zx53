from . import *

class Pokemon(Base):
  __tablename__ = 'pokemons'

  name = db.Column(db.String(128), nullable =False, unique =True)
  attack = db.Column(db.Integer, nullable=False)
  capture_rate =  db.Column(db.Integer, nullable=False)
  defense = db.Column(db.Integer, nullable=False)
  hp = db.Column(db.Integer, nullable=False)
  pokedex_number = db.Column(db.Integer, nullable=False)
  sp_attack = db.Column(db.Integer, nullable=False)
  sp_defense = db.Column(db.Integer, nullable=False)
  speed = db.Column(db.Integer, nullable=False)
  type1 = db.Column(db.String(128), nullable =False, unique =True)
  type2 = db.Column(db.String(128), nullable =False, unique =True)
  generation = db.Column(db.Integer, nullable=False)
  is_legendary = db.Column(db.Integer, nullable=False)
  #image =  #figure something for image


  def __init__(self, **kwargs):

    self.name = kwargs.get('name', None)
    self.attack = kwargs.get('attack', None)
    self.capture_rate = kwargs.get('capture_rate', None)
    self.defense = kwargs.get('defense', None)
    self.hp = kwargs.get('hp', None)
    self.pokedex_number = kwargs.get('pokedex_number', None)
    self.sp_attack = kwargs.get('sp_attack', None)
    self.sp_defense = kwargs.get('sp_defense', None)
    self.sp_speed = kwargs.get('sp_speed', None)
    self.speed = kwargs.get('speed', None)
    self.type1 = kwargs.get('type1', None)
    self.type2 = kwargs.get('type2', None)
    self.generation = kwargs.get('generation', None)
    self.is_legendary = kwargs.get('is_legendary', None)
    self.image = kwargs.get('image', None)


  def __repr__(self):
    return str(self.__dict__)




class PokemonSchema(ModelSchema):
  class Meta:
    model = Pokemon
