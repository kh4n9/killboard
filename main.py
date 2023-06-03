import requests
import json

class item:
    def __init__(self, Type, Count, Quality, ActiveSpells, PassiveSpells):
        self.Type = Type
        self.Count = Count
        self.Quality = Quality
        self.ActiveSpells = ActiveSpells
        self.PassiveSpells = PassiveSpells

class PVE:
    def __init__(self, Total, Royal, Outlands, Avalon, Hellgate, CorruptedDungeon, Mists):
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
class GatherRing:
    def __init__(self, Filber, Hide, Ore, Rock, Wood, All):
        self.Filber = Filber
        self.Hide = Hide
        self.Ore = Ore
        self.Rock = Rock
        self.Wood = Wood
        self.All = All

class Crafting:
    def __init__(self, Avalon, Outlands, Royal, Total):
        self.Avalon = Avalon
        self.Outlands = Outlands
        self.Royal = Royal
        self.Total = Total

class LifetimeStatistics:
    def __init__(self, Crafting, CrystalLeague, FarmingFame, FishingFame, Gathering, PVE, Timestamp):
        self.Crafting = Crafting
        self.CrystalLeague = CrystalLeague
        self.FarmingFame = FarmingFame
        self.FishingFame = FishingFame
        self.Gathering = Gathering
        self.PVE = PVE
        self.Timestamp = Timestamp

class Equipment:
    def __init__(self, Armor, Bag, Cap, Food, Head, MainHand, Mount, OffHand, Potion, Shoes):
        self.Armor = Armor
        self.Bag = Bag
        self.Cap = Cap
        self.Food = Food
        self.Head = Head
        self.MainHand = MainHand
        self.Mount = Mount
        self.OffHand = OffHand
        self.Potion = Potion
        self.Shoes = Shoes

class people:
    def __init__(self, AverageItemPower, Equipment, Inventory, Name, Id, GuildName, GuildId, AllianceName, AllianceId, AllianceTag, Avatar, AvatarRing, DeathFame, KillFame, FameRatio, LifetimeStatistics):
        self.AverageItemPower = AverageItemPower
        self.Equipment = Equipment
        self.Inventory = Inventory
        self.Name = Name
        self.Id = Id
        self.GuildName = GuildName
        self.GuildId = GuildId
        self.AllianceName = AllianceName
        self.AllianceId = AllianceId
        self.AllianceTag = AllianceTag
        self.Avatar = Avatar
        self.AvatarRing = AvatarRing
        self.DeathFame = DeathFame
        self.KillFame = KillFame
        self.FameRatio = FameRatio
        self.LifetimeStatistics = LifetimeStatistics
        

class Battle:
    def __init__(self, groupMemberCount, numberOfParticipants, EventId, TimeStamp, Version, Killer, Victim, TotalVictimKillFame, Location, Participants, GroupMembers, GvGMatch, BattleId, KillArea, Category, Type):
        self.groupMemberCount = groupMemberCount
        self.numberOfParticipants = numberOfParticipants
        self.EventId = EventId
        self.TimeStamp = TimeStamp
        self.Version = Version
        self.Killer = Killer
        self.Victim = Victim
        self.TotalVictimKillFame = TotalVictimKillFame
        self.Location = Location
        self.Participants = Participants
        self.GroupMembers = GroupMembers
        self.GvGMatch = GvGMatch
        self.BattleId = BattleId
        self.KillArea = KillArea
        self.Category = Category
        self.Type = Type


class Json:
    def __init__(self):
        self.url = 'https://gameinfo.albiononline.com/api/gameinfo/events?limit=51&offset=0'
        self.rp = requests.get(self.url)
    def get_string(self):
        return self.rp.text
    

def main():
    js = Json()
    js = json.loads(js.get_string())
    for i in js:
        print(i['Killer']['Name'], ' ', i['BattleId'], ' ', i['TimeStamp'], '\n')

main()