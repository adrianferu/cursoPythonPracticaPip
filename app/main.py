import utils
import read_csv
import charts
import pandas as pd

def run():
  # '''
  # data = list(filter(lambda item : item['Continent'] == 'South America',data)) #Filtra valores que correspondan con Sudamerica
  # countries = list(map(lambda x: x['Country'], data))
  # percentages = list(map(lambda x: x['World Population Percentage'], data))
  # '''

  ''' Esto es igual a esto de abajo'''

  #Crear dataframe
  df = pd.read_csv('data.csv')
  dfSudamerica = df[df['Continent'] == 'Asia']
  #Filtrer Series
  countries = df['Country'].values
  percentages = df['World Population Percentage'].values


  charts.generate_pie_chart(countries, percentages)

  data = read_csv.read_csv('data.csv')
  country = input('Type Country => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], labels, values)

  ''' Comentamos toda esta secuencia para demostrar como se puede hacer lo mismo
  en Pandas.'''

if __name__ == '__main__':
  run()