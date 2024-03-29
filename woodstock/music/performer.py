"""Domain classes and functions related to the concept of performer
"""


from woodstock.util import utility
from woodstock.music.enums import Vocals, Instrument

import json


class Performer:
    """The class describing the concept of performer.
    It is assumed that a performer is sufficiently described by their
    name and whether they are a solo performer or a band.

    Illustrates some of the important concepts of Python classes:
    - self
    - __init__()
    - __str__()
    - __eq__(self, other) is the equivalent of Java equals() and should be overridden in classes
    - data fields (instance variables)
    - methods - calling them by self.<method>(...) from the same class where they are defined
    """

    def __init__(self, name, is_band=True):
        self.name = name
        self.is_band = is_band
        # self.__n = 'lll'                                    # 'private' field

    # Properties: 'private' fields; run setters and getters in the debugger.
    # Make name a property (after setting up __init__(), __str__(), __eq__(), methods,...).

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n if isinstance(n, str) and n != '' else 'unknown'

    # Add an immutable property (no setter for it)

    def __str__(self):
        return (self.name + ' (band)' if self.is_band else self.name + ' (solo performer)') \
            if self.name and isinstance(self.name, str) and self.name != 'unknown' else 'unknown'

    def __eq__(self, other):
        return self.name == other.name

    def play(self, song_title, *args, **kwargs):
        """Assumes that song_title, *args (expressions of gratitude) and kwargs.values() (messages) are strings.
        Prints song_title, expressions of gratitude and messages. A call example:
            <performer>.play(song_title, *['Thank you!', 'You're wonderful!], love='We love you!')
        """

        print(self.name + ':', song_title + '...', ' '.join(args), ' '.join([v for k, v in kwargs.items()]))

    def play_song(self, song_title, *args, **kwargs):
        """Demonstrates calling another method feom the same class (self.<method>(...) as a mandatory syntax).
        """

        self.play(song_title, *args, **kwargs)

    # Alternative constructor
    @classmethod
    def from_str(cls, performer_string):
        """Inverted __str__() method.
        Assumes that performer_string is in the format generated by __str__().
        """

        split = performer_string.split(' (')
        name = split[0]
        is_band = True
        if split[0] == 'unknown':
            name = ''
            is_band = False
        if split[-1] == 'solo performer)':
            is_band = False
        return cls(name, is_band)


class PerformerEncoder(json.JSONEncoder):
    """JSON encoder for Performer objects.
    """

    def default(self, o):
        # recommendation: always use double quotes with JSON
        if isinstance(o, Performer):
            return {"__Performer__": o.__dict__}
        return {f"__{o.__class__.__name__}__": o.__dict__}

        # if isinstance(o, Performer):
        #     d = o.__dict__.copy()


def performer_json_to_py(performer_json):
    """JSON decoder for Performer objects (object_hook parameter in json.loads()).
    """

    if "__Performer__" in performer_json:
        p = Performer('')
        p.__dict__.update(performer_json["__Performer__"])
        return p
    return performer_json


class Singer(Performer):
    """The class describing the concept of singer.
    It is assumed that a singer is sufficiently described as a Performer,
    with the addition of whether they are a lead or a background singer.
    """

    # # Version 1 - no multiple inheritance
    # def __init__(self, name, vocals, is_band=False):
    #     super().__init__(name, is_band=is_band)
    #     self.vocals = vocals if isinstance(vocals, Vocals) else None

    # Version 2 - no multiple inheritance
    def __init__(self, vocals, **kwargs):
        super().__init__(**kwargs)
        self.vocals = vocals if isinstance(vocals, Vocals) else None

    def __str__(self):
        return super().__str__() + \
               (f', {self.vocals.name.lower().replace("_", " ")}' if isinstance(self.vocals, Vocals) else '')

    def __eq__(self, other):
        return self == other if isinstance(other, Singer) else False

    def play(self, song_title, *args, **kwargs):
        """Overrides the play() method from superclass.
        Assumes that song_title, *args (expressions of gratitude) and kwargs.values() (messages) are strings.
        Prints song_title, expressions of gratitude and messages. A call example:
            <singer>.play(song_title, *['Thank you!', 'You're wonderful!'], love='We love you!')
        """

        # super().play(song_title, *args, **kwargs)
        print(self.name + ' singing:', song_title + '...', ' '.join(args), ' '.join([v for k, v in kwargs.items()]))


class Songwriter(Performer):
    """The class describing the concept of songwriter.
    It is assumed that a songwriter is sufficiently described as a Performer
    who writes songs and plays an instrument.
    """

    # # Version 1 - no multiple inheritance
    # def __init__(self, name, instrument, is_band=False):
    #     super().__init__(name, is_band=is_band)
    #     self.instrument = instrument
    #     self.writes_songs = True

    # Version 2 - with multiple inheritance
    def __init__(self, instrument, **kwargs):
        super().__init__(**kwargs)
        self.instrument = instrument
        self.writes_songs = True

    def __str__(self):
        return f'{self.name}, songwriter ({self.instrument.name.lower().replace("_", " ")})'

    def __eq__(self, other):
        return self == other if isinstance(other, Songwriter) else False

    def what_do_you_do(self):
        """Just a simple method to describe the concept of songwriter.
        """

        print(f'I\'m a songwriter' if self.writes_songs else f'I play {self.instrument}')


class SingerSongwriter(Singer, Songwriter):
    """The class describing the concept of singer-songwriter.
    It is assumed that a singer-songwriter is sufficiently described as a Singer who is simultaneously a Songwriter.
    """

    # def __init__(self, name, vocals, **kwargs):
    #     super().__init__(name, vocals, **kwargs)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __str__(self):
        return super().__str__() + ', singer-songwriter'


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

    # Print objects
    print(theBand)
    print()

    # Compare objects
    print(theWho == Performer('Paul Butterfield Blues Band'))
    print()

    # Access data fields (instance variables), including 'private' fields
    jimiHendrix.name = 'Jimi Hendrix Experience'
    print(jimiHendrix.name)
    print(jimiHendrix)
    # print(jimiHendrix._Performer__n)
    print()

    # Add new data fields (instance variables)
    #   1. <object>.<new_attr> = <value>
    #   2. <object>.__setattr__('<new_attr>', <value>)      # counterpart: <object>.__getattribute__('<attr>')
    #   3. setattr(<object>, '<new_attr>', <value>))        # counterpart: getattr(<object>, '<attr>')
    # jimiHendrix.nationality = 'US'
    # jimiHendrix.__setattr__('nationality', 'US')
    # print(jimiHendrix.nationality)
    # print(jimiHendrix.__getattribute__('nationality'))
    setattr(jimiHendrix, 'nationality', 'US')
    print(getattr(jimiHendrix, 'nationality'))
    print(getattr(jimiHendrix, 'name'))
    print()

    # Calling methods
    jimiHendrix.play('Crosstown traffic', *['Thank you!', 'Yeah!'], love='We love you!')
    jimiHendrix.play_song('Crosstown traffic', *['Thank you!', 'Yeah!'], love='We love you!')
    print()

    # Demonstrate object data fields and methods in Python Console for some built-in classes (boolean, int, object,...)
    # - True + 1
    # - True.__int__()
    # - (1).__class__.__name__
    # - (1).__class__
    # - o.__dir__()
    # - o.__dir__

    # Demonstrate object data fields and methods in Python Console for Performer objects
    print(jimiHendrix.__dict__)
    print(jimiHendrix.__dir__())
    print()

    # Demonstrate @classmethod (from_str())
    jimiHendrixStr = jimiHendrix.__str__()
    print(Performer.from_str(jimiHendrixStr))
    unknown_performer = Performer('')
    print(unknown_performer)
    unknown_performer_str = unknown_performer.__str__()
    print(Performer.from_str(unknown_performer_str))
    print()

    # Demonstrate inheritance
    rogerDaltrey = Singer(name='Roger Daltrey', vocals=Vocals.LEAD_VOCALS, is_band=False)
    print(rogerDaltrey)
    peteTownshend = Songwriter(name='Pete Townshend', instrument=Instrument.LEAD_GUITAR, is_band=False)
    print(peteTownshend)
    print()

    # Demonstrate method overriding
    rogerDaltrey.play('See Me, Feel Me', *['Thank you!', 'You\'re wonderful!'], love='We love you!')
    print()

    # Demonstrate multiple inheritance and MRO.
    # Make sure to read this first: https://stackoverflow.com/a/50465583/1899061 (especially Scenario 3).
    arloGuthrie = SingerSongwriter(name='Arlo Guthrie',
                                   vocals=Vocals.LEAD_VOCALS,
                                   is_band=False,
                                   instrument=Instrument.LEAD_GUITAR)
    print(arloGuthrie)
    print()

    # Demonstrate JSON encoding/decoding of Performer objects
    # Single object
    # print(json.dumps([1, None, 2.3, 'wer', {'2': 'two', '3': 'three'}, True], indent=4))
    # print(json.dumps(23, indent=4))
    csny_json = json.dumps(csny, cls=PerformerEncoder, indent=4)
    print(csny_json)
    p = json.loads(csny_json, object_hook=performer_json_to_py)
    print(p)

    print()

    # List of objects
    day2_performers = [gratefulDead, jeffersonAirplane, theWho, ccr]
    day2_json = json.dumps(day2_performers, cls=PerformerEncoder, indent=4)
    print(day2_json)
    p_list = json.loads(day2_json, object_hook=performer_json_to_py)
    for p in p_list:
        print(p)
    print()


