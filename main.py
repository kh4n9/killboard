import requests
import json
url = 'https://gameinfo.albiononline.com/api/gameinfo/events?limit=3&offset=0'

class item:
    def __init__(self, Type, Count, Quality, ActiveSpells, PassiveSpells):
        self.Type = Type
        self.Count = Count
        self. Quality = Quality
        self.ActiveSpells = ActiveSpells
        self.PassiveSpells = PassiveSpells

class PVE:
    def __init__(self, Total, Royal, Outlands, Avalon, Hellgate, CorruptedDungeon, Mists)
        self.Total = Total
        self.Royal = Royal
        self.OutLands = Outlands
        self.Avalon = Avalon
        self.Hellgate = Hellgate
        self.CorruptedDungeon = CorruptedDungeon
        self.Mists = Mists 

class ItemGathering:
    def __init__(self, Total, Royal, Outlands, Avalon):
        self.Total = Total
        self.Royal = Royal
        self.Outlands = Outlands
        self.Avalon = Avalon

class Filber(ItemGathering):
    def __init__(self, Total, Royal, Outlands, Avalon):
        super().__init__(Total, Royal, Outlands, Avalon)

class Hide(ItemGathering):
    def __init__(self, Total, Royal, Outlands, Avalon):
        super().__init__(Total, Royal, Outlands, Avalon)

class Ore(ItemGathering):
    def __init__(self, Total, Royal, Outlands, Avalon):
        super().__init__(Total, Royal, Outlands, Avalon)

class Rock(ItemGathering):
    def __init__(self, Total, Royal, Outlands, Avalon):
        super().__init__(Total, Royal, Outlands, Avalon)

class Wood(ItemGathering):
    def __init__(self, Total, Royal, Outlands, Avalon):
        super().__init__(Total, Royal, Outlands, Avalon)

class All(ItemGathering):
    def __init__(self, Total, Royal, Outlands, Avalon):
        super().__init__(Total, Royal, Outlands, Avalon)
class GatherRing

class LifetimeStatistics:
    def __init__(self, PVE, ):
        self.PVE = PVE

class people:
    def __init__(self, AverageItemPower, Equipment, Inventory, Name, Id, GuildName, GuildId, AllianceName, AllianceId, AllianceTag, Avatar, AvatarRing, DeathFame, KillFame, FameRatio, LifetimeStatistics)

class Battle:
    def __init__(self, groupMemberCount, numberOfParticipants, EventId, TimeStamp, Version, Killer, Victim, TotalVictimKillFame, Location, Participants, GroupMembers, GvGMatch, BattleId, KillArea, Category, Type):
        self.groupMemberCount = groupMemberCount
        self.numberOfParticipants = numberOfParticipants
        self.EventId = EventId
        self.TimeStamp = TimeStamp
        self.Version = Version
        self.AverageItemPower = Killer['AverageItemPower']

        self.Victim
        self.TotalVictimKillFame = TotalVictimKillFame
        self.Location = Location
        self.Participants
        self.GroupMembers
        self.GvGMatch = GvGMatch
        self.BattleId = BattleId
        self.KillArea = KillArea
        self.Category = Category
        self.Type = Type

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)
    
    def __repr__(self):
        return f'<Battle {self.AverageItemPower}>'