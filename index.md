# covid19-tracker

## Installation

Run the following to install:
```python
pip install covid19-tracker 
```

## Usage

```python
 from covid19tracker import Tracker

 track = Tracker() 
```

### Get Total Worldwide Cases 
```python
 track.total_cases()
```
Output:
```
25992115
```

### Get Total Worldwide deaths 
```python
 track.total_deaths()
```
Output:
```
862773
```

### Get Total Worldwide Recoveries 
```python
 track.total_recoveries()
```
Output:
```
18261000
```

### Get Worldwide Active cases
```python
 track.active_cases()
```
Output:
```
{
   'currently infected patients': 6866475,
   'patients in mild conditions': 6805920,
   'serious/critical conditions': 60555
}
```

### Get Worldwide Closed cases
```python
 track.closed_cases()
```
Output:
```
{
   'outcomes': 19142009,
   'recovered/discharged': 18278873,
   'deaths': 863136
}
```

### Get Country names
```python
 track.countries() 
```
Output:
```
[
   'USA',
   'Brazil',
   'India', 
   'Russia',
   'Peru',
   'Colombia',
   'South Africa',
   'Mexico',
   'Spain',
   'Argentina',
   'Chile',
   'Iran',
   'UK'
   ... 
]
```

### Get Country Information using name
```python
 track.country_info_by_name('india')
```
Output:
```
{
   'id': 3,
   'name': 'India',
   'total cases': 3810625,
   'new cases': 44517,
   'total deaths': 66871,
   'new deaths': 411,
   'total recoveries': 2931005,
   'new recoveries': 31484,
   'active cases': 812749,
   'critical cases': 8944,
   'total cases/1M pop': 2757,
   'deaths/1M pop': 48,
   'total tests/1M pop': 44337201,
   'tests/1M pop': 32075,
   'population': 1382308045,
   'continent': 'Asia',
   '1 case every X ppl': 363,
   '1 death every X ppl': 20671,
   '1 test every X ppl': 31
}
```

### Get Country Information using id
```
 track.country_info_by_id(2)
```
Output:
```
{
   'id': 2,
   'name': 'Brazil',
   'total cases': 3952790,
   'new cases': 'N/A',
   'total deaths': 122681,
   'new deaths': 'N/A',
   'total reciveries': 3159096,
   'new recoveries': 'N/A',
   'active cases': 671013,
   'critical cases': 8318,
   'total cases/1M pop': 18574,
   'deaths/1M pop': 576,
   'total tests/1M pop': 14352484,
   'tests/1M pop': 67440,
   'population': 212817864,
   'continent': 'South America',
   '1 case every X ppl': 54,
   '1 death every X ppl': 1735, 
   '1 test every X ppl': 15
}
```

### Get Continent Information
```python
 track.continent_info('Asia') 
```
Output:
```
{
   'name': 'Asia', 
   'total cases': 7266345,
   'new cases': 77856,
   'total deaths': 145247,
   'new deaths': 1160,
   'total recoveries': 5832330,
   'new recoveries': 64220,
   'active cases': 1288768,
   'critical cases': 18821
}
```

### Get Information of all countries belonging to a continent
```python
 track.countries_info_by_continent('europe')
```
Output:
```
[
   {
      'id': 4,
      'name': 'Russia',
      'total cases': 1005000,
      'new cases': 4952,
      'total deaths': 17414,
      'new deaths': 115,
      'total recoveries': 821169,
      'new recoveries': 5464,
      'active cases': 166417,
      'critical cases': 2300, 
      'total cases/1M pop': 6886,
      'deaths/1M pop': 119,
      'total tests/1M pop': 37100000,
      'tests/1M pop': 254205,
      'population': 145945354,
      'continent': 'Europe',
      '1 case every X ppl': 145,
      '1 death every X ppl': 8381,
      '1 test every X ppl': 4
   },
   {
      'id': 9,
      'name': 'Spain',
      'total cases': 1005000,
      'new cases': 4952,
      'total deaths': 17414,
      'new deaths': 115,
      'total recoveries': 821169,
      'new recoveries': 5464,
      'active cases': 166417,
      'critical cases': 2300,
      'total cases/1M pop': 6886,
      'deaths/1M pop': 119,
      'total tests/1M pop': 37100000,
      'tests/1M pop': 254205,
      'population': 145945354,
      'continent': 'Europe',
      '1 case every X ppl': 145,
      '1 death every X ppl': 8381,
      '1 test every X ppl': 4
   }
   ... 
]
```

### Get Symptoms
```python
 from covid19-tracker import covid
 covid.symptoms() 
```
Output:
```
 Most common symptoms:
   • fever
   • dry cough
   • tiredness
 Less common symptoms:
   • aches and pains
   • sore throat
   • diarrhoea
   • conjunctivitis
   • headache
   • loss of taste or smell
   • a rash on skin, or discolouration of fingers or toes
```

### Get Prevention Methods
```python
 covid.preventions()
```
Output:
```
Protect yourself and others around you by knowing the facts and taking appropriate precautions. Follow advice provided by your local health authority.

To prevent the spread of COVID-19:
   • Clean your hands often. Use soap and water, or an alcohol-based hand rub.
   • Maintain a safe distance from anyone who is coughing or sneezing.
   • Wear a mask when physical distancing is not possible.
   • Don’t touch your eyes, nose or mouth.
   • Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.
   • Stay home if you feel unwell.
   • If you have a fever, cough and difficulty breathing, seek medical attention.

Calling in advance allows your healthcare provider to quickly direct you to the right health facility. This protects you, and prevents the spread of viruses and other infections.

Masks

Masks can help prevent the spread of the virus from the person wearing the mask to others. Masks alone do not protect against COVID-19, and should be combined with physical distancing and hand hygiene. Follow the advice provided by your local health authority.
```
