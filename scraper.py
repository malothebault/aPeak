import requests
from bs4 import BeautifulSoup

#url = "https://www.surf-sentinel.com/surf-report/france/ille-et-vilaine/saint-malo/le-sillon"
#url = "https://www.surf-sentinel.com/surf-report/france/finistere/plomeur/la-torche"

def get_quality_dict(url):
    req = requests.get(url)

    soup = BeautifulSoup(req.text, features="html.parser")

    daily_notes = soup.find_all("tr", class_="note-row")

    quality_match = {'A': 4,
                    'B': 3,
                    'C': 2,
                    'D': 1,
                    'E': 0,}

    output_dict = {}

    for day, dn in enumerate(daily_notes):
        day = int(day)
        notes = dn.find_all(class_="note")
        output_dict[day] = {}
        for hour, note in enumerate(notes):
            hour = int(hour)
            quality, size = list(note.text.strip())
            quality = quality_match[quality]
            output_dict[day][hour] = {'quality':quality,
                                    'size':int(size),}
    return output_dict


# with open('data.json', 'w', encoding='utf-8') as f:
#     json.dump(output_dict, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    url = "https://www.surf-sentinel.com/surf-report/france/ille-et-vilaine/saint-malo/le-sillon"
    output_dict = get_quality_dict(url)
    print(output_dict[0][0])