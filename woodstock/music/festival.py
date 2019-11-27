"""The class representing the concept of a festival.
"""

from datetime import date
import sys
from pickle import dump, load

from woodstock.music.performer import *
from woodstock.music.lineup import *
from woodstock.util.utility import *


class Festival:
    """The class describing the concept of a festival.
    It includes a name, a list of Lineup objects (lineups by date), location and the start and end dates.
    """

    def __init__(self, name, location, start, end, *lineups):
        if start > end:
            raise FestivalStartDateException(start, end)
        elif not all([check_lineup_date(lineup, start, end) for lineup in lineups]):
            wrong_dates = [lineup.date for lineup in lineups if not check_lineup_date(lineup, start, end)]
            raise LineupDateException(wrong_dates[0], start, end)
        else:
            self.name = name if name and isinstance(name, str) else 'unknown'
            self.location = location if location and isinstance(location, str) else 'unknown'
            self.start = start if start and isinstance(start, date) else 'unknown'
            self.end = end if end and isinstance(end, date) else 'unknown'
            self.lineups = lineups if lineups and all([isinstance(lineup, Lineup) for lineup in lineups]) else 'unknown'

    def __str__(self):
        first_line = f'{self.name} ({format_date(self.start)} - {format_date(self.end)}), {self.location}'
        lineups = '\n\t'.join(str(lineup) for lineup in self.lineups)
        return first_line + '\n\t' + lineups


class FestivalError(Exception):
    """Base class for exceptions in this module.
    """

    pass


class FestivalStartDateException(FestivalError):
    """Exception raised when a the tart date of a festival lineup is not between start and end dates of the festival.
    """

    def __init__(self, start, end):
        self.message = f'start date ({format_date(start)}) after end date ({format_date(end)})'


def check_lineup_date(lineup, start_date, end_date):
    """Checks if lineup.date is between start_date and end_date."""

    return start_date <= lineup.date <= end_date


class LineupDateException(FestivalError):
    """Exception raised when a the date of a festival lineup is not between start and end dates of the festival.
    """

    def __init__(self, d, start_date, end_date):
        self.message = f'lineup date ({d}) not between start ({start_date}) and end ({end_date}) dates'


class FestivalEncoder(json.JSONEncoder):
    """JSON encoder for Festival objects.
    """

    def default(self, o):
        # recommendation: always use double quotes with JSON

        if isinstance(o, Festival):
            f = o.__dict__.copy()
            f["lineups"] = json.dumps(f["lineups"], cls=LineupEncoder, indent=4)
            f["start"] = date.isoformat(f["start"])
            f["end"] = date.isoformat(f["end"])
            return {"__Festival__": f}
        return {f"__{o.__class__.__name__}__": o.__dict__}


def festival_json_to_py(festival_json):
    """JSON decoder for Festival objects (object_hook parameter in json.loads()).
    """

    if "__Festival__" in festival_json:
        f = Festival('', '', date.today(), date.today())
        f.__dict__.update(festival_json["__Festival__"])
        f.start = date.fromisoformat(f.start)
        f.end = date.fromisoformat(f.end)
        f.lineups = tuple(json.loads(f.lineups, object_hook=lineup_json_to_py))
        return f
    return festival_json


if __name__ == "__main__":

    pass

    # Data

    # Some of the Woodstock performers, Aug 15-16, 1969
    melanie = Performer('Melanie', is_band=False)
    arloGuthrie = Performer('Arlo Guthrie', is_band=False)
    # Some of the Woodstock performers, Aug 16-17, 1969
    gratefulDead = Performer('Grateful Dead', is_band=True)
    jeffersonAirplane = Performer('Jefferson Airplane', is_band=True)
    theWho = Performer('The Who', is_band=True)
    ccr = Performer('Creedence Clearwater Revival', is_band=True)
    # Some of the Woodstock performers, Aug 17-18, 1969
    csny = Performer('Crosby, Stills, Nash and Young', is_band=True)
    jimiHendrix = Performer('Jimi Hendrix', is_band=False)
    theBand = Performer('The Band', is_band=True)

    day1_performers = [melanie, arloGuthrie]
    day1_lineup = Lineup(*day1_performers, date=date(1969, 8, 15))
    day2_performers = [gratefulDead, jeffersonAirplane, theWho, ccr]
    day2_lineup = Lineup(*day2_performers, date=date(1969, 8, 16))
    day3_performers = [csny, jimiHendrix, theBand]
    day3_lineup = Lineup(*day3_performers, date=date(1969, 8, 17))

    # Create a Festival object
    # woodstock = Festival('Woodstock', 'Bethel, NY', date(1969, 8, 15), date(1969, 8, 17),
    #                      day1_lineup, day2_lineup, day3_lineup)
    # print(woodstock)
    print()

    # Demonstrate exceptions
    # Here's the hierarchy of built-in exceptions: https://docs.python.org/3/library/exceptions.html#exception-hierarchy

    # Demonstrate exceptions - the general structure of try-except statements, possibly including else and finally
    d2_performers = ['Grateful Dead', 'Jefferson Airplane', 'The Who', 'Creedence Clearwater Revival']
    # try:
    #     print(d2_performers[4])
    # except:
    #     # print('Caught an exception')
    #     sys.stderr.write('Caught an exception')
    #     # raise
    # else:
    #     print('This is else...')
    # finally:
    #     print('This is finally...')
    # print()

    # Demonstrate exceptions - except: <exception> as <e> (and then type(<e>), <e>.__class__.__name__, <e>.args,...)
    # try:
    #     print(d2_performers[4])
    # except IndexError as e:
    #     # print('Caught an exception')
    #     # sys.stderr.write(f'Caught an {e.__class__.__name__} exception')
    #     sys.stderr.write(f'Caught an {e.__class__.__name__} exception: {e.args[0]}')
    #     # print(type(e))
    #     # print(e.args)
    #     # raise
    # print()

    # Demonstrate exceptions - user-defined exceptions (wrong festival date(s), wrong lineup date)
    try:
        woodstock = Festival('Woodstock', 'Bethel, NY', date(1969, 8, 15), date(1969, 8, 17),
                             day1_lineup, day2_lineup, day3_lineup)
    except FestivalStartDateException as e:
        sys.stderr.write(f'{e.__class__.__name__}: {e.message}\n')
    except LineupDateException as e:
        sys.stderr.write(f'{e.__class__.__name__}: {e.message}\n')
    else:
        print(woodstock)
    print()

    # # Demonstrate writing to a text file
    # with open('outfile.txt', 'w') as f:
    #     f.write(str(arloGuthrie))
    # print()

    # Demonstrate reading from a text file
    # with open('outfile.txt', 'r') as f:
    #     # print(f.readline())
    #     print(str(Performer.from_str(f.readline())))
    # print()

    # Demonstrate writing to a binary file - pickle.dump() and <f>.write()/<f>.writelines() with str.encode(<obj>)
    # with open('outfile', 'wb') as f:
    #     dump(arloGuthrie, f)
    # print()

    # Demonstrate reading from a binary file - pickle.load() and <f>.read().decode()/<f>.readlines().decode()
    # with open('outfile', 'rb') as f:
    #     p = load(f)
    #     print(p)
    # print()

    # Demonstrate get_project_dir(), get_data_dir() and writing/reading to/from files in data dir
    # print('get_project_dir():', get_project_dir())
    # print('get_data_dir():', get_data_dir())
    # with open(get_data_dir() / 'outfile.txt', 'w') as f:
    #     f.write(str(arloGuthrie))
    # print()

    # Demonstrate JSON encoding/decoding of Festival objects
    # Single object
    woodstock = Festival('Woodstock', 'Bethel, NY', date(1969, 8, 15), date(1969, 8, 17),
                         day1_lineup, day2_lineup, day3_lineup)
    woodstock_json = json.dumps(woodstock, cls=FestivalEncoder, indent=4)
    print(woodstock_json)
    print()

    # List of objects
    woodstock = json.loads(woodstock_json, object_hook=festival_json_to_py)
    print(woodstock)
    print()



