from telethon import TelegramClient, events, Button
from telethon.tl.types import InputMediaDocument
from telethon.tl.custom import Message
import time
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
import asyncio
import random
import math
import requests


api_id = "27715449"
api_hash = "dd3da7c5045f7679ff1f0ed0c82404e0"
bot_token = "8180632650:AAHZeMhhuyT2_ai6b9WX2qd_YoofZskEmeY"

poke_moves = ['10,000,000 Volt Thunderbolt', 'Absorb', 'Accelerock', 'Acid', 'Acid Armor', 'Acid Downpour', 'Acid Spray', 'Acrobatics', 'Acupressure', 'Aerial Ace', 'Aeroblast', 'After You', 'Agility', 'Air Cutter', 'Air Slash', 'All-Out Pummeling', 'Alluring Voice', 'Ally Switch', 'Amnesia', 'Anchor Shot', 'Ancient Power', 'Apple Acid', 'Aqua Cutter', 'Aqua Jet', 'Aqua Ring', 'Aqua Step', 'Aqua Tail', 'Arm Thrust', 'Armor Cannon', 'Aromatherapy', 'Aromatic Mist', 'Assist', 'Assurance', 'Astonish', 'Astral Barrage', 'Attack Order', 'Attract', 'Aura Sphere', 'Aura Wheel', 'Aurora Beam', 'Aurora Veil', 'Autotomize', 'Avalanche', 'Axe Kick', 'Baby-Doll Eyes', 'Baddy Bad', 'Baneful Bunker', 'Barb Barrage', 'Barrage', 'Barrier', 'Baton Pass', 'Beak Blast', 'Beat Up', 'Behemoth Bash', 'Behemoth Blade', 'Belch', 'Belly Drum', 'Bestow', 'Bide', 'Bind', 'Bite', 'Bitter Blade', 'Bitter Malice', 'Black Hole Eclipse', 'Blast Burn', 'Blaze Kick', 'Blazing Torque', 'Bleakwind Storm', 'Blizzard', 'Block', 'Blood Moon', 'Bloom Doom', 'Blue Flare', 'Body Press', 'Body Slam', 'Bolt Beak', 'Bolt Strike', 'Bone Club', 'Bone Rush', 'Bonemerang', 'Boomburst', 'Bounce', 'Bouncy Bubble', 'Branch Poke', 'Brave Bird', 'Breaking Swipe', 'Breakneck Blitz', 'Brick Break', 'Brine', 'Brutal Swing', 'Bubble', 'Bubble Beam', 'Bug Bite', 'Bug Buzz', 'Bulk Up', 'Bulldoze', 'Bullet Punch', 'Bullet Seed', 'Burn Up', 'Burning Bulwark', 'Burning Jealousy', 'Buzzy Buzz', 'Calm Mind', 'Camouflage', 'Captivate', 'Catastropika', 'Ceaseless Edge', 'Celebrate', 'Charge', 'Charge Beam', 'Charm', 'Chatter', 'Chilling Water', 'Chilly Reception', 'Chip Away', 'Chloroblast', 'Circle Throw', 'Clamp', 'Clanging Scales', 'Clangorous Soul', 'Clangorous Soulblaze', 'Clear Smog', 'Close Combat', 'Coaching', 'Coil', 'Collision Course', 'Combat Torque', 'Comet Punch', 'Comeuppance', 'Confide', 'Confuse Ray', 'Confusion', 'Constrict', 'Continental Crush', 'Conversion', 'Conversion 2', 'Copycat', 'Core Enforcer', 'Corkscrew Crash', 'Corrosive Gas', 'Cosmic Power', 'Cotton Guard', 'Cotton Spore', 'Counter', 'Court Change', 'Covet', 'Crabhammer', 'Crafty Shield', 'Cross Chop', 'Cross Poison', 'Crunch', 'Crush Claw', 'Crush Grip', 'Curse', 'Cut', 'Dark Pulse', 'Dark Void', 'Darkest Lariat', 'Dazzling Gleam', 'Decorate', 'Defend Order', 'Defense Curl', 'Defog', 'Destiny Bond', 'Detect', 'Devastating Drake', 'Diamond Storm', 'Dig', 'Dire Claw', 'Disable', 'Disarming Voice', 'Discharge', 'Dive', 'Dizzy Punch', 'Doodle', 'Doom Desire', 'Double Hit', 'Double Iron Bash', 'Double Kick', 'Double Shock', 'Double Slap', 'Double Team', 'Double-Edge', 'Draco Meteor', 'Dragon Ascent', 'Dragon Breath', 'Dragon Cheer', 'Dragon Claw', 'Dragon Dance', 'Dragon Darts', 'Dragon Energy', 'Dragon Hammer', 'Dragon Pulse', 'Dragon Rage', 'Dragon Rush', 'Dragon Tail', 'Drain Punch', 'Draining Kiss', 'Dream Eater', 'Drill Peck', 'Drill Run', 'Drum Beating', 'Dual Chop', 'Dual Wingbeat', 'Dynamax Cannon', 'Dynamic Punch', 'Earth Power', 'Earthquake', 'Echoed Voice', 'Eerie Impulse', 'Eerie Spell', 'Egg Bomb', 'Electric Terrain', 'Electrify', 'Electro Ball', 'Electro Drift', 'Electro Shot', 'Electroweb', 'Embargo', 'Ember', 'Encore', 'Endeavor', 'Endure', 'Energy Ball', 'Entrainment', 'Eruption', 'Esper Wing', 'Eternabeam', 'Expanding Force', 'Explosion', 'Extrasensory', 'Extreme Evoboost', 'Extreme Speed', 'Facade', 'Fairy Lock', 'Fairy Wind', 'Fake Out', 'Fake Tears', 'False Surrender', 'False Swipe', 'Feather Dance', 'Feint', 'Feint Attack', 'Fell Stinger', 'Fickle Beam', 'Fiery Dance', 'Fiery Wrath', 'Fillet Away', 'Final Gambit', 'Fire Blast', 'Fire Fang', 'Fire Lash', 'Fire Pledge', 'Fire Punch', 'Fire Spin', 'First Impression', 'Fishious Rend', 'Fissure', 'Flail', 'Flame Burst', 'Flame Charge', 'Flame Wheel', 'Flamethrower', 'Flare Blitz', 'Flash', 'Flash Cannon', 'Flatter', 'Fleur Cannon', 'Fling', 'Flip Turn', 'Floaty Fall', 'Floral Healing', 'Flower Shield', 'Flower Trick', 'Fly', 'Flying Press', 'Focus Blast', 'Focus Energy', 'Focus Punch', 'Follow Me', 'Force Palm', 'Foresight', "Forest's Curse", 'Foul Play','Freeze Shock', 'Freeze-Dry', 'Freezing Glare', 'Freezy Frost', 'Frenzy Plant', 'Frost Breath', 'Frustration', 'Fury Attack', 'Fury Cutter', 'Fury Swipes', 'Fusion Bolt', 'Fusion Flare', 'Future Sight', 'G-Max Befuddle', 'G-Max Cannonade', 'G-Max Centiferno', 'G-Max Chi Strike', 'G-Max Cuddle', 'G-Max Depletion', 'G-Max Drum Solo', 'G-Max Finale', 'G-Max Fireball', 'G-Max Foam Burst', 'G-Max Gold Rush', 'G-Max Gravitas', 'G-Max Hydrosnipe', 'G-Max Malodor', 'G-Max Meltdown', 'G-Max One Blow', 'G-Max Rapid Flow', 'G-Max Replenish', 'G-Max Resonance', 'G-Max Sandblast', 'G-Max Smite', 'G-Max Snooze', 'G-Max Steelsurge', 'G-Max Stonesurge', 'G-Max Stun Shock', 'G-Max Sweetness', 'G-Max Tartness', 'G-Max Terror', 'G-Max Vine Lash', 'G-Max Volcalith', 'G-Max Volt Crash', 'G-Max Wildfire', 'G-Max Wind Rage', 'Gastro Acid', 'Gear Grind', 'Gear Up', 'Genesis Supernova', 'Geomancy', 'Giga Drain', 'Giga Impact', 'Gigaton Hammer', 'Gigavolt Havoc', 'Glacial Lance', 'Glaciate', 'Glaive Rush', 'Glare', 'Glitzy Glow', 'Grass Knot', 'Grass Pledge', 'Grass Whistle', 'Grassy Glide', 'Grassy Terrain', 'Grav Apple', 'Gravity', 'Growl', 'Growth', 'Grudge', 'Guard Split', 'Guard Swap', 'Guardian of Alola', 'Guillotine', 'Gunk Shot', 'Gust', 'Gyro Ball', 'Hail', 'Hammer Arm', 'Happy Hour', 'Hard Press', 'Harden', 'Haze', 'Head Charge', 'Head Smash', 'Headbutt', 'Headlong Rush', 'Heal Bell', 'Heal Block', 'Heal Order', 'Heal Pulse', 'Healing Wish', 'Heart Stamp', 'Heart Swap', 'Heat Crash', 'Heat Wave', 'Heavy Slam', 'Helping Hand', 'Hex', 'Hidden Power', 'High Horsepower', 'High Jump Kick', 'Hold Back', 'Hold Hands', 'Hone Claws', 'Horn Attack', 'Horn Drill', 'Horn Leech', 'Howl', 'Hurricane', 'Hydro Cannon', 'Hydro Pump', 'Hydro Steam', 'Hydro Vortex', 'Hyper Beam', 'Hyper Drill', 'Hyper Fang', 'Hyper Voice', 'Hyperspace Fury', 'Hyperspace Hole', 'Hypnosis', 'Ice Ball', 'Ice Beam', 'Ice Burn', 'Ice Fang', 'Ice Hammer', 'Ice Punch', 'Ice Shard', 'Ice Spinner', 'Icicle Crash', 'Icicle Spear', 'Icy Wind', 'Imprison', 'Incinerate', 'Infernal Parade', 'Inferno', 'Inferno Overdrive', 'Infestation', 'Ingrain', 'Instruct', 'Ion Deluge', 'Iron Defense', 'Iron Head', 'Iron Tail', 'Ivy Cudgel', 'Jaw Lock', 'Jet Punch', 'Judgment', 'Jump Kick', 'Jungle Healing', 'Karate Chop', 'Kinesis', "King's Shield", 'Knock Off', 'Kowtow Cleave', "Land's Wrath", 'Laser Focus', 'Lash Out', 'Last Resort', 'Last Respects', 'Lava Plume', 'Leaf Blade', 'Leaf Storm', 'Leaf Tornado', 'Leafage', 'Leech Life', 'Leech Seed', 'Leer', "Let's Snuggle Forever", 'Lick', 'Life Dew', 'Light of Ruin', 'Light Screen', 'Light That Burns the Sky', 'Liquidation', 'Lock-On', 'Lovely Kiss', 'Low Kick', 'Low Sweep', 'Lucky Chant', 'Lumina Crash', 'Lunar Blessing', 'Lunar Dance', 'Lunge', 'Luster Purge', 'Mach Punch', 'Magic Coat', 'Magic Powder', 'Magic Room', 'Magical Leaf', 'Magical Torque', 'Magma Storm', 'Magnet Bomb', 'Magnet Rise', 'Magnetic Flux', 'Magnitude', 'Make It Rain', 'Malicious Moonsault', 'Malignant Chain', 'Mat Block', 'Matcha Gotcha', 'Max Airstream', 'Max Darkness', 'Max Flare', 'Max Flutterby', 'Max Geyser', 'Max Guard', 'Max Hailstorm', 'Max Knuckle', 'Max Lightning', 'Max Mindstorm', 'Max Ooze', 'Max Overgrowth', 'Max Phantasm', 'Max Quake', 'Max Rockfall', 'Max Starfall', 'Max Steelspike', 'Max Strike', 'Max Wyrmwind', 'Me First', 'Mean Look', 'Meditate', 'Mega Drain', 'Mega Kick', 'Mega Punch', 'Megahorn', 'Memento', 'Menacing Moonraze Maelstrom', 'Metal Burst', 'Metal Claw', 'Metal Sound', 'Meteor Assault', 'Meteor Beam', 'Meteor Mash', 'Metronome', 'Mighty Cleave', 'Milk Drink', 'Mimic', 'Mind Blown', 'Mind Reader', 'Minimize', 'Miracle Eye', 'Mirror Coat', 'Mirror Move', 'Mirror Shot', 'Mist', 'Mist Ball', 'Misty Explosion', 'Misty Terrain', 'Moonblast', 'Moongeist Beam', 'Moonlight', 'Morning Sun', 'Mortal Spin', 'Mountain Gale', 'Mud Bomb', 'Mud Shot', 'Mud Sport', 'Mud-Slap', 'Muddy Water', 'Multi-Attack', 'Mystical Fire', 'Mystical Power', 'Nasty Plot', 'Natural Gift', 'Nature Power', "Nature's Madness", 'Needle Arm', 'Never-Ending Nightmare', 'Night Daze','Night Shade', 'Night Slash', 'Nightmare', 'No Retreat', 'Noble Roar', 'Noxious Torque', 'Nuzzle', 'Oblivion Wing', 'Obstruct', 'Oceanic Operetta', 'Octazooka', 'Octolock', 'Odor Sleuth', 'Ominous Wind', 'Order Up', 'Origin Pulse', 'Outrage', 'Overdrive', 'Overheat', 'Pain Split', 'Parabolic Charge', 'Parting Shot', 'Pay Day', 'Payback', 'Peck', 'Perish Song', 'Petal Blizzard', 'Petal Dance', 'Phantom Force', 'Photon Geyser', 'Pika Papow', 'Pin Missile', 'Plasma Fists', 'Play Nice', 'Play Rough', 'Pluck', 'Poison Fang', 'Poison Gas', 'Poison Jab', 'Poison Powder', 'Poison Sting', 'Poison Tail', 'Pollen Puff', 'Poltergeist', 'Population Bomb', 'Pounce', 'Pound', 'Powder', 'Powder Snow', 'Power Gem', 'Power Shift', 'Power Split', 'Power Swap', 'Power Trick', 'Power Trip', 'Power Whip', 'Power-Up Punch', 'Precipice Blades', 'Present', 'Prismatic Laser', 'Protect', 'Psybeam', 'Psyblade', 'Psych Up', 'Psychic', 'Psychic Fangs', 'Psychic Noise', 'Psychic Terrain', 'Psycho Boost', 'Psycho Cut', 'Psycho Shift', 'Psyshield Bash', 'Psyshock', 'Psystrike', 'Psywave', 'Pulverizing Pancake', 'Punishment', 'Purify', 'Pursuit', 'Pyro Ball', 'Quash', 'Quick Attack', 'Quick Guard', 'Quiver Dance', 'Rage', 'Rage Fist', 'Rage Powder', 'Raging Bull', 'Raging Fury', 'Rain Dance', 'Rapid Spin', 'Razor Leaf', 'Razor Shell', 'Razor Wind', 'Recover', 'Recycle', 'Reflect', 'Reflect Type', 'Refresh', 'Relic Song', 'Rest', 'Retaliate', 'Return', 'Revelation Dance', 'Revenge', 'Reversal', 'Revival Blessing', 'Rising Voltage', 'Roar', 'Roar of Time', 'Rock Blast', 'Rock Climb', 'Rock Polish', 'Rock Slide', 'Rock Smash', 'Rock Throw', 'Rock Tomb', 'Rock Wrecker', 'Role Play', 'Rolling Kick', 'Rollout', 'Roost', 'Rototiller', 'Round', 'Ruination', 'Sacred Fire', 'Sacred Sword', 'Safeguard', 'Salt Cure', 'Sand Attack', 'Sand Tomb', 'Sandsear Storm', 'Sandstorm', 'Sappy Seed', 'Savage Spin-Out', 'Scald', 'Scale Shot', 'Scary Face', 'Scorching Sands', 'Scratch', 'Screech', 'Searing Shot', 'Searing Sunraze Smash', 'Secret Power', 'Secret Sword', 'Seed Bomb', 'Seed Flare', 'Seismic Toss', 'Self-Destruct', 'Shadow Ball', 'Shadow Bone', 'Shadow Claw', 'Shadow Force', 'Shadow Punch', 'Shadow Sneak', 'Sharpen', 'Shattered Psyche', 'Shed Tail', 'Sheer Cold', 'Shell Side Arm', 'Shell Smash', 'Shell Trap', 'Shelter', 'Shift Gear', 'Shock Wave', 'Shore Up', 'Signal Beam', 'Silk Trap', 'Silver Wind', 'Simple Beam', 'Sing', 'Sinister Arrow Raid', 'Sizzly Slide', 'Sketch', 'Skill Swap', 'Skitter Smack', 'Skull Bash', 'Sky Attack', 'Sky Drop', 'Sky Uppercut', 'Slack Off', 'Slam', 'Slash', 'Sleep Powder', 'Sleep Talk', 'Sludge', 'Sludge Bomb', 'Sludge Wave', 'Smack Down', 'Smart Strike', 'Smelling Salts', 'Smog', 'Smokescreen', 'Snap Trap', 'Snarl', 'Snatch', 'Snipe Shot', 'Snore', 'Snowscape', 'Soak', 'Soft-Boiled', 'Solar Beam', 'Solar Blade', 'Sonic Boom', 'Soul-Stealing 7-Star Strike', 'Spacial Rend', 'Spark', 'Sparkling Aria', 'Sparkly Swirl', 'Spectral Thief', 'Speed Swap', 'Spicy Extract', 'Spider Web', 'Spike Cannon', 'Spikes', 'Spiky Shield', 'Spin Out', 'Spirit Break', 'Spirit Shackle', 'Spit Up', 'Spite', 'Splash', 'Splintered Stormshards', 'Splishy Splash', 'Spore', 'Spotlight', 'Springtide Storm', 'Stealth Rock', 'Steam Eruption', 'Steamroller', 'Steel Beam', 'Steel Roller', 'Steel Wing', 'Sticky Web', 'Stockpile', 'Stoked Sparksurfer', 'Stomp', 'Stomping Tantrum', 'Stone Axe', 'Stone Edge', 'Stored Power', 'Storm Throw', 'Strange Steam', 'Strength', 'Strength Sap', 'String Shot', 'Struggle', 'Struggle Bug', 'Stuff Cheeks', 'Stun Spore', 'Submission', 'Substitute', 'Subzero Slammer', 'Sucker Punch', 'Sunny Day', 'Sunsteel Strike', 'Super Fang', 'Supercell Slam', 'Superpower', 'Supersonic', 'Supersonic Skystrike', 'Surf', 'Surging Strikes', 'Swagger', 'Swallow', 'Sweet Kiss', 'Sweet Scent', 'Swift', 'Switcheroo', 'Swords Dance', 'Synchronoise', 'Synthesis', 'Syrup Bomb', 'Tachyon Cutter', 'Tackle', 'Tail Glow', 'Tail Slap', 'Tail Whip', 'Tailwind', 'Take Down', 'Take Heart', 'Tar Shot', 'Taunt', 'Tearful Look', 'Teatime', 'Techno Blast', 'Tectonic Rage','Teeter Dance', 'Telekinesis', 'Teleport', 'Temper Flare', 'Tera Blast', 'Tera Starstorm', 'Terrain Pulse', 'Thief', 'Thousand Arrows', 'Thousand Waves', 'Thrash', 'Throat Chop', 'Thunder', 'Thunder Cage', 'Thunder Fang', 'Thunder Punch', 'Thunder Shock', 'Thunder Wave', 'Thunderbolt', 'Thunderclap', 'Thunderous Kick', 'Tickle', 'Tidy Up', 'Topsy-Turvy', 'Torch Song', 'Torment', 'Toxic', 'Toxic Spikes', 'Toxic Thread', 'Trailblaze', 'Transform', 'Tri Attack', 'Trick', 'Trick Room', 'Trick-or-Treat', 'Triple Arrows', 'Triple Axel', 'Triple Dive', 'Triple Kick', 'Trop Kick', 'Trump Card', 'Twin Beam', 'Twineedle', 'Twinkle Tackle', 'Twister', 'U-turn', 'Upper Hand', 'Uproar', 'V-create', 'Vacuum Wave', 'Veevee Volley', 'Venom Drench', 'Venoshock', 'Victory Dance', 'Vine Whip', 'Vise Grip', 'Vital Throw', 'Volt Switch', 'Volt Tackle', 'Wake-Up Slap', 'Water Gun', 'Water Pledge', 'Water Pulse', 'Water Shuriken', 'Water Sport', 'Water Spout', 'Waterfall', 'Wave Crash', 'Weather Ball', 'Whirlpool', 'Whirlwind', 'Wicked Blow', 'Wicked Torque', 'Wide Guard', 'Wild Charge', 'Wildbolt Storm', 'Will-O-Wisp', 'Wing Attack', 'Wish', 'Withdraw', 'Wonder Room', 'Wood Hammer', 'Work Up', 'Worry Seed', 'Wrap', 'Wring Out', 'X-Scissor', 'Yawn', 'Zap Cannon', 'Zen Headbutt', 'Zing Zap', 'Zippy Zap']
# MongoDB setup
MONGODB_URL = "mongodb+srv://PokemonMasters:Sarvesh2369@cluster0.qzem0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
MONGO = MongoClient(MONGODB_URL)
db = MONGO['Pokemon-Masters-DB']
col = db['users']

# Create the Telegram bot client
app = TelegramClient('wsdfghj', api_id, api_hash)

#user credentials
app.user_states={}
user_battle = {}
async def test_mongo_connection():
    try:
        # Perform a test query to check if the connection is established
        await db.command("ping")
        print("MongoDB connection successful!")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
current_indices = {}
async def users():
  return[6735548827,5611071586,7503471575,7730460768,1017904439,7946913230,6632519077,1947921832]


#source file_ids
error_image="AgACAgUAAxkBAAIHomeDfoCnF7o3a5k54vHc28acgGLzAAJEwjEbQoaZV4i1LLdR5I66AAgBAAMCAAN4AAceBA"
logo_image="AgACAgUAAxkBAAIH7meEo3fG_pW71jBgpKlTp2s40pEtAAJvwDEb3FFAVzsPv5vliMtPAAgBAAMCAAN4AAceBA"
connect_image="AgACAgUAAxkBAAIIG2eE4bAhOYOZawIEfjoKxfpa47LMAAJrvTEb9LspVBRHlvhLuwfcAAgBAAMCAAN5AAceBA"
version_image="AgACAgUAAxkBAAIKG2eKRXczSDoE-GYIioMVM4x8YwvvAAKqvzEbVAvAVyGmRLTy0pGgAAgBAAMCAAN5AAceBA"
pending_video="BAACAgUAAxkBAAIKeWeLtXUFriwGv5cGqZtKcRw9-ulEAAJSEAACFiDIV6q6kmrlvE3bHgQ"

#Media files
boy_white="AgACAgUAAxkBAAIJ0WeI4nOrtEP5AzO4Evu_p0o5NkE1AAIhzjEbmE55VwSzkNv2eUTWAAgBAAMCAAN5AAceBA"
boy_white_hair="AgACAgUAAxkBAAIJ0meI4nNZvf_WPBxPnsrwXskpoRCTAAIizjEbmE55V1YkqkyGGJdPAAgBAAMCAAN5AAceBA"
boy_light_black="AgACAgUAAxkBAAIJ02eI4nOyb2EQ-jRrviGUci8kV9hkAAIjzjEbmE55V5USnz75OTRcAAgBAAMCAAN5AAceBA"
boy_dark="AgACAgUAAxkBAAIJ1GeI4nN7ucx9AlD1oEjAg4rEGMbIAAIkzjEbmE55V4Q1zWjcBU5NAAgBAAMCAAN5AAceBA"
girl_white="AgACAgUAAxkBAAIJ1WeI4nMtO82NDQ05_ppHveFIlVU0AAInzjEbmE55VzOsDsm5du46AAgBAAMCAAN5AAceBA"
girl_white_hair="AgACAgUAAxkBAAIJ1meI4nNKpnjoewFdy8joIPMrx95lAAIqzjEbmE55V5Sms1pkGTtgAAgBAAMCAAN5AAceBA"
girl_light_black="AgACAgUAAxkBAAIJ12eI4nPnEwtSi5Qc1EjaM8axAQ20AAIuzjEbmE55V4z4sZ8rPHukAAgBAAMCAAN5AAceBA"
girl_dark="AgACAgUAAxkBAAIJ2GeI4nOvbUbg30MywSaUcuJe_7XFAAIvzjEbmE55VzGbscFYZ621AAgBAAMCAAN5AAceBA"

characters = [
    {"name": "boy_white", "url": "AgACAgUAAxkBAAIJ0WeI4nOrtEP5AzO4Evu_p0o5NkE1AAIhzjEbmE55VwSzkNv2eUTWAAgBAAMCAAN5AAceBA"},
    {"name": "boy_white_hair", "url": "AgACAgUAAxkBAAIJ0meI4nNZvf_WPBxPnsrwXskpoRCTAAIizjEbmE55V1YkqkyGGJdPAAgBAAMCAAN5AAceBA"},
    {"name": "boy_light_black", "url": "AgACAgUAAxkBAAIJ02eI4nOyb2EQ-jRrviGUci8kV9hkAAIjzjEbmE55V5USnz75OTRcAAgBAAMCAAN5AAceBA"},
    {"name": "boy_dark", "url": "AgACAgUAAxkBAAIJ1GeI4nN7ucx9AlD1oEjAg4rEGMbIAAIkzjEbmE55V4Q1zWjcBU5NAAgBAAMCAAN5AAceBA"},
    {"name": "girl_white", "url": "AgACAgUAAxkBAAIJ1WeI4nMtO82NDQ05_ppHveFIlVU0AAInzjEbmE55VzOsDsm5du46AAgBAAMCAAN5AAceBA"},
    {"name": "girl_white_hair", "url": "AgACAgUAAxkBAAIJ1meI4nNKpnjoewFdy8joIPMrx95lAAIqzjEbmE55V5Sms1pkGTtgAAgBAAMCAAN5AAceBA"},
    {"name": "girl_light_black", "url": "AgACAgUAAxkBAAIJ12eI4nPnEwtSi5Qc1EjaM8axAQ20AAIuzjEbmE55V4z4sZ8rPHukAAgBAAMCAAN5AAceBA"},
    {"name": "girl_dark", "url": "AgACAgUAAxkBAAIJ2GeI4nOvbUbg30MywSaUcuJe_7XFAAIvzjEbmE55VzGbscFYZ621AAgBAAMCAAN5AAceBA"},
]

PRIVATE_GROUP_ID = -1002388846235 # Example: Private group ID
VIDEO_MESSAGE_ID = 1571

# Start time
StartTime = time.time()

# Command prefixes
prefix = [".", "!", "?", "*", "$", "#", "/"]

def hp_bar(cur_hp, full_hp):
    # Calculate the percentage of current HP
    if full_hp <= 0:
        raise ValueError("full_hp must be greater than 0")
    
    percentage = (cur_hp / full_hp) * 100
    
    # Calculate the number of filled boxes (■) and empty boxes (□)
    filled_boxes = min(10, max(0, int(percentage // 10)))  # Max 10 boxes
    empty_boxes = 10 - filled_boxes
    
    # Create the HP bar string
    hp_bar_string = "■" * filled_boxes + "□" * empty_boxes
    
    return hp_bar_string


def get_partner_pokemon_data(user_data):
    try:
        
        party_data = user_data.get("party", {}).get("1") 
        if not party_data:
            print("No pokemon data found in party!")
            return None
        
        pokemon_id_to_find = party_data.get("id")
        if not pokemon_id_to_find:
             print("No pokemon_id in party object!")
             return None
        
        pokemon_data_object = user_data.get("Pokemon", {}) 
        
        for pokemon_name, pokemon_data in pokemon_data_object.items(): 
           if pokemon_data.get("pokemon_id") == pokemon_id_to_find:
                return pokemon_data
            
        print(f"Partner pokemon with ID '{pokemon_id_to_find}' not found in pokemon data.")
        return None
    except json.JSONDecodeError:
        print("Invalid JSON Data")
        return None


def fetch_data():
    response = requests.get("https://nintendrolocationapi.onrender.com/locations")
    return response.json()

async def get_spawn(location):
    # Fetch Pokémon data for the location
    data = fetch_data()
    pokemon_data = data["locations"]["kanto"].get(location, {})
    
    if not pokemon_data:
        return "No Pokémon data available for this location."

    # Calculate total spawn rate
    total_spawn_rate = sum(pokemon["spawn_rate"] for pokemon in pokemon_data.values())
    
    # Generate a random number between 1 and the total spawn rate
    rand = random.randint(1, total_spawn_rate)
    
    # Determine which Pokémon spawns based on the random number
    cumulative_rate = 0
    for pokemon, info in pokemon_data.items():
        cumulative_rate += info["spawn_rate"]
        if rand <= cumulative_rate:
            
            min_level, max_level = map(int, info["level"].split("-"))
            level = random.randint(min_level, max_level)
            return f"Oh! You encountered a wild {pokemon.capitalize()} (Level {level})"

#class for partner-pokemon


class PartnerPokemon:
    def __init__(self, url,pokemon_url):
        self.url = url
        self.data = self._fetch_data()
        self.pokemon_url = pokemon_url

    def _fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {self.url}: {e}")
            return {}

    def get_name(self):
        return self.data.get("Basic_Info", {}).get("Name", "Unknown")
    def get_id(self):
        return self.data.get("Basic_Info",{}).get("National_Id", "Unknown")
    def get_type(self):
        return self.data.get("Basic_Info",{}).get("Type", "Unknown")
    def fetch_abilities_from_pokemon(self):
        # Send a request to the Pokemon URL to get the Pokemon data
        response = requests.get(self.pokemon_url)
        if response.status_code == 200:
            pokemon_data = response.json()
            return pokemon_data['abilities']  # Extract the abilities from the response
        else:
            print(f"Error fetching data from {self.pokemon_url}")
            return []
    def extract_abilities(self):
        abilities = {}
        ability_data = self.fetch_abilities_from_pokemon()

        # Loop through abilities
        for idx, ability_info in enumerate(ability_data):
            ability_name = ability_info['ability']['name']
            is_hidden = ability_info['is_hidden']
            
            # Format the abilities into the required structure
            if is_hidden:
                abilities['hidden_ability'] = ability_name
            else:
                # Check if it's the first or second ability
                if 'ability1' not in abilities:
                    abilities['ability1'] = ability_name
                elif 'ability2' not in abilities:
                    abilities['ability2'] = ability_name
        
        return abilities
    def generate_pokemon_id(self):
        timestamp = int(time.time())  # Current timestamp in seconds
        random_number = random.randint(1000, 9999)  # Random number for added uniqueness
        unique_id = f"POKEMON_{timestamp}_{random_number}"
        return unique_id
    def get_category(self):
        return self.data.get("Basic_Info",{}).get("Category", "Unknown")
    def get_description(self):
        return self.data.get("Basic_Info",{}).get("Description", "Unknown")
    def get_nature(self):
        natures = ["Adamant","Bashful","Bold","Brave","Calm","Careful","Docile","Gentle","Hardy","Hasty","Impish","Jolly","Lax","Lonely","Mild","Modest","Naughty","Quiet","Quirky","Rash","Relaxed","Sassy","Serious","Timid"]
        natures = random.sample(natures, 1)
        global nature
        nature = "lonely"#natures[0]
        return nature
    def get_ivs(self):
        x=[26,27,28,29,30,31]
        ivs={
            "hp":random.choice  (x),
            "atk":random.choice(x),
            "def":random.choice(x),
            "spa":random.choice(x),
            "spd":random.choice(x),
            "spe":random.choice(x),
        }
        global hp_iv,atk_iv,def_iv,spa_iv,spd_iv,spe_iv 
        hp_iv,atk_iv,def_iv,spa_iv,spd_iv,spe_iv = ivs["hp"],ivs["atk"],ivs["def"],ivs["spa"],ivs["spd"],ivs["spe"]
        return ivs
    def get_evs(self):
        evs={
            "hp":0,
            "atk":0,
            "def":0,
            "spa":0,
            "spd":0,
            "spe":0,
        }
        global hp_ev,atk_ev,def_ev,spa_ev,spd_ev,spe_ev 
        hp_ev,atk_ev,def_ev,spa_ev,spd_ev,spe_ev = evs["hp"],evs["atk"],evs["def"],evs["spa"],evs["spd"],evs["spe"]
        return evs
    def get_moves(self):
        moves = self.data.get("Moves",{}).get("Level_up_Moves", [])
        x=[
            move for move in moves
            if move.get("level") is not None and int(move["level"]) < 5
        ]
        y=x[-4:]
        return y
    def get_stats(self):
        hp_base_stat = self.data.get("Base_Stats",{}).get("Hp","unknown")
        atk_base_stat = self.data.get("Base_Stats",{}).get("Attack","unknown")
        def_base_stat = self.data.get("Base_Stats",{}).get("Defence","unknown")
        spa_base_stat = self.data.get("Base_Stats",{}).get("Sp.Attack","unknown")
        spd_base_stat = self.data.get("Base_Stats",{}).get("Sp.Defence","unknown")
        spe_base_stat = self.data.get("Base_Stats",{}).get("Speed","unknown")
        hp_base_stat = int(hp_base_stat)
        atk_base_stat = int(atk_base_stat)
        def_base_stat = int(def_base_stat)
        spa_base_stat = int(spa_base_stat)
        spd_base_stat = int(spd_base_stat)
        spe_base_stat = int(spe_base_stat)
        level = 5
        
        if nature == "hardy":
            hp_stat = (((2*hp_base_stat+hp_iv+(hp_ev//4) +100) / 100)*level)+10
            hp_stat = math.floor(hp_stat)
            atk_stat = ((((2*atk_base_stat+atk_iv+(atk_ev//4))/100)*level)+5)*1
            atk_stat = math.floor(atk_stat)
            def_stat = (((2*def_base_stat+def_iv+(def_ev//4))/100)*level)+5*1
            def_stat = math.floor(def_stat)
            spa_stat = (((2*spa_base_stat+spa_iv+(spa_ev//4))/100)*level)+5*1
            spa_stat = math.floor(spa_stat)
            spd_stat = (((2*spd_base_stat+spd_iv+(spd_ev//4))/100)*level)+5*1
            spd_stat = math.floor(spd_stat)
            spe_stat = (((2*spe_base_stat+spe_iv+(spe_ev//4))/100)*level)+5*1
            spe_stat = math.floor(spe_stat)
        elif nature == "lonely":
            hp_stat = (((2*hp_base_stat+hp_iv+(hp_ev//4) +100) / 100)*level)+10
            hp_stat = math.floor(hp_stat)
            atk_stat = (((2*atk_base_stat+atk_iv+(atk_ev//4))/100)*level)+5*1.1
            atk_stat = math.floor(atk_stat)
            def_stat = (((2*def_base_stat+def_iv+(def_ev//4))/100)*level)+5*0.9
            def_stat = math.floor(def_stat)
            spa_stat = (((2*spa_base_stat+spa_iv+(spa_ev//4))/100)*level)+5*1
            spa_stat = math.floor(spa_stat)
            spd_stat = (((2*spd_base_stat+spd_iv+(spd_ev//4))/100)*level)+5*1
            spd_stat = math.floor(spd_stat)
            spe_stat = (((2*spe_base_stat+spe_iv+(spe_ev//4))/100)*level)+5*1
            spe_stat = math.floor(spe_stat)
        elif nature == "brave":
            hp_stat = (((2*hp_base_stat+hp_iv+(hp_ev//4) +100) / 100)*level)+10
            hp_stat = math.floor(hp_stat)
            atk_stat = ((((2*atk_base_stat+atk_iv+(atk_ev//4))/100)*level)+5)*1.1
            atk_stat = math.floor(atk_stat)
            def_stat = (((2*def_base_stat+def_iv+(def_ev//4))/100)*level)+5*1
            def_stat = math.floor(def_stat)
            spa_stat = (((2*spa_base_stat+spa_iv+(spa_ev//4))/100)*level)+5*1
            spa_stat = math.floor(spa_stat)
            spd_stat = (((2*spd_base_stat+spd_iv+(spd_ev//4))/100)*level)+5*1
            spd_stat = math.floor(spd_stat)
            spe_stat = (((2*spe_base_stat+spe_iv+(spe_ev//4))/100)*level)+5*0.9
            spe_stat = math.floor(spe_stat)
        elif nature == "adamant":
            hp_stat = (((2*hp_base_stat+hp_iv+(hp_ev//4) +100) / 100)*level)+10
            hp_stat = math.floor(hp_stat)
            atk_stat = ((((2*atk_base_stat+atk_iv+(atk_ev//4))/100)*level)+5)*1.1
            atk_stat = math.floor(atk_stat)
            def_stat = (((2*def_base_stat+def_iv+(def_ev//4))/100)*level)+5*1
            def_stat = math.floor(def_stat)
            spa_stat = (((2*spa_base_stat+spa_iv+(spa_ev//4))/100)*level)+5*0.9
            spa_stat = math.floor(spa_stat)
            spd_stat = (((2*spd_base_stat+spd_iv+(spd_ev//4))/100)*level)+5*1
            spd_stat = math.floor(spd_stat)
            spe_stat = (((2*spe_base_stat+spe_iv+(spe_ev//4))/100)*level)+5*1
            spe_stat = math.floor(spe_stat)
        elif nature == "naughty":
            hp_stat = (((2*hp_base_stat+hp_iv+(hp_ev//4) +100) / 100)*level)+10
            hp_stat = math.floor(hp_stat)
            atk_stat = ((((2*atk_base_stat+atk_iv+(atk_ev//4))/100)*level)+5)*1.1
            atk_stat = math.floor(atk_stat)
            def_stat = (((2*def_base_stat+def_iv+(def_ev//4))/100)*level)+5*1
            def_stat = math.floor(def_stat)
            spa_stat = (((2*spa_base_stat+spa_iv+(spa_ev//4))/100)*level)+5*1
            spa_stat = math.floor(spa_stat)
            spd_stat = (((2*spd_base_stat+spd_iv+(spd_ev//4))/100)*level)+5*0.9
            spd_stat = math.floor(spd_stat)
            spe_stat = (((2*spe_base_stat+spe_iv+(spe_ev//4))/100)*level)+5*1
            spe_stat = math.floor(spe_stat)
        elif nature == "bold":
            hp_stat = (((2*hp_base_stat+hp_iv+(hp_ev//4) +100) / 100)*level)+10
            hp_stat = math.floor(hp_stat)
            atk_stat = ((((2*atk_base_stat+atk_iv+(atk_ev//4))/100)*level)+5)*0.9
            atk_stat = math.floor(atk_stat)
            def_stat = (((2*def_base_stat+def_iv+(def_ev//4))/100)*level)+5*1.1
            def_stat = math.floor(def_stat)
            spa_stat = (((2*spa_base_stat+spa_iv+(spa_ev//4))/100)*level)+5*1
            spa_stat = math.floor(spa_stat)
            spd_stat = (((2*spd_base_stat+spd_iv+(spd_ev//4))/100)*level)+5*1
            spd_stat = math.floor(spd_stat)
            spe_stat = (((2*spe_base_stat+spe_iv+(spe_ev//4))/100)*level)+5*1
            spe_stat = math.floor(spe_stat)
        elif nature == "docile":
            hp_stat = (((2*hp_base_stat+hp_iv+(hp_ev//4) +100) / 100)*level)+10
            hp_stat = math.floor(hp_stat)
            atk_stat = ((((2*atk_base_stat+atk_iv+(atk_ev//4))/100)*level)+5)*1
            atk_stat = math.floor(atk_stat)
            def_stat = (((2*def_base_stat+def_iv+(def_ev//4))/100)*level)+5*1
            def_stat = math.floor(def_stat)
            spa_stat = (((2*spa_base_stat+spa_iv+(spa_ev//4))/100)*level)+5*1
            spa_stat = math.floor(spa_stat)
            spd_stat = (((2*spd_base_stat+spd_iv+(spd_ev//4))/100)*level)+5*1
            spd_stat = math.floor(spd_stat)
            spe_stat = (((2*spe_base_stat+spe_iv+(spe_ev//4))/100)*level)+5*1
            spe_stat = math.floor(spe_stat)
        elif nature == "relaxed":
            hp_stat = (((2*hp_base_stat+hp_iv+(hp_ev//4) +100) / 100)*level)+10
            hp_stat = math.floor(hp_stat)
            atk_stat = ((((2*atk_base_stat+atk_iv+(atk_ev//4))/100)*level)+5)*1
            atk_stat = math.floor(atk_stat)
            def_stat = (((2*def_base_stat+def_iv+(def_ev//4))/100)*level)+5*1.1
            def_stat = math.floor(def_stat)
            spa_stat = (((2*spa_base_stat+spa_iv+(spa_ev//4))/100)*level)+5*1
            spa_stat = math.floor(spa_stat)
            spd_stat = (((2*spd_base_stat+spd_iv+(spd_ev//4))/100)*level)+5*1
            spd_stat = math.floor(spd_stat)
            spe_stat = (((2*spe_base_stat+spe_iv+(spe_ev//4))/100)*level)+5*0.9
            spe_stat = math.floor(spe_stat)
        elif nature == "impish":
            hp_stat = (((2*hp_base_stat+hp_iv+(hp_ev//4) +100) / 100)*level)+10
            hp_stat = math.floor(hp_stat)
            atk_stat = ((((2*atk_base_stat+atk_iv+(atk_ev//4))/100)*level)+5)*1
            atk_stat = math.floor(atk_stat)
            def_stat = (((2*def_base_stat+def_iv+(def_ev//4))/100)*level)+5*1.1
            def_stat = math.floor(def_stat)
            spa_stat = (((2*spa_base_stat+spa_iv+(spa_ev//4))/100)*level)+5*0.9
            spa_stat = math.floor(spa_stat)
            spd_stat = (((2*spd_base_stat+spd_iv+(spd_ev//4))/100)*level)+5*1
            spd_stat = math.floor(spd_stat)
            spe_stat = (((2*spe_base_stat+spe_iv+(spe_ev//4))/100)*level)+5*1
            spe_stat = math.floor(spe_stat)
        elif nature == "lax":
            hp_stat = (((2*hp_base_stat+hp_iv+(hp_ev//4) +100) / 100)*level)+10
            hp_stat = math.floor(hp_stat)
            atk_stat = ((((2*atk_base_stat+atk_iv+(atk_ev//4))/100)*level)+5)*1
            atk_stat = math.floor(atk_stat)
            def_stat = (((2*def_base_stat+def_iv+(def_ev//4))/100)*level)+5*1.1
            def_stat = math.floor(def_stat)
            spa_stat = (((2*spa_base_stat+spa_iv+(spa_ev//4))/100)*level)+5*1
            spa_stat = math.floor(spa_stat)
            spd_stat = (((2*spd_base_stat+spd_iv+(spd_ev//4))/100)*level)+5*0.9
            spd_stat = math.floor(spd_stat)
            spe_stat = (((2*spe_base_stat+spe_iv+(spe_ev//4))/100)*level)+5*1
            spe_stat = math.floor(spe_stat)
        elif nature == "timid":
            hp_stat = (((2*hp_base_stat+hp_iv+(hp_ev//4) +100) / 100)*level)+10
            hp_stat = math.floor(hp_stat)
            atk_stat = ((((2*atk_base_stat+atk_iv+(atk_ev//4))/100)*level)+5)*0.9
            atk_stat = math.floor(atk_stat)
            def_stat = (((2*def_base_stat+def_iv+(def_ev//4))/100)*level)+5*1
            def_stat = math.floor(def_stat)
            spa_stat = (((2*spa_base_stat+spa_iv+(spa_ev//4))/100)*level)+5*1
            spa_stat = math.floor(spa_stat)
            spd_stat = (((2*spd_base_stat+spd_iv+(spd_ev//4))/100)*level)+5*1
            spd_stat = math.floor(spd_stat)
            spe_stat = (((2*spe_base_stat+spe_iv+(spe_ev//4))/100)*level)+5*1.1
            spe_stat = math.floor(spe_stat)
        elif nature == "hasty":
            hp_stat = (((2*hp_base_stat+hp_iv+(hp_ev//4) +100) / 100)*level)+10
            hp_stat = math.floor(hp_stat)
            atk_stat = ((((2*atk_base_stat+atk_iv+(atk_ev//4))/100)*level)+5)*1
            atk_stat = math.floor(atk_stat)
            def_stat = (((2*def_base_stat+def_iv+(def_ev//4))/100)*level)+5*0.9
            def_stat = math.floor(def_stat)
            spa_stat = (((2*spa_base_stat+spa_iv+(spa_ev//4))/100)*level)+5*1
            spa_stat = math.floor(spa_stat)
            spd_stat = (((2*spd_base_stat+spd_iv+(spd_ev//4))/100)*level)+5*1
            spd_stat = math.floor(spd_stat)
            spe_stat = (((2*spe_base_stat+spe_iv+(spe_ev//4))/100)*level)+5*1.1
            spe_stat = math.floor(spe_stat)
        elif nature == "serious":
            hp_stat = (((2*hp_base_stat+hp_iv+(hp_ev//4) +100) / 100)*level)+10
            hp_stat = math.floor(hp_stat)
            atk_stat = ((((2*atk_base_stat+atk_iv+(atk_ev//4))/100)*level)+5)*1
            atk_stat = math.floor(atk_stat)
            def_stat = (((2*def_base_stat+def_iv+(def_ev//4))/100)*level)+5*1
            def_stat = math.floor(def_stat)
            spa_stat = (((2*spa_base_stat+spa_iv+(spa_ev//4))/100)*level)+5*1
            spa_stat = math.floor(spa_stat)
            spd_stat = (((2*spd_base_stat+spd_iv+(spd_ev//4))/100)*level)+5*1
            spd_stat = math.floor(spd_stat)
            spe_stat = (((2*spe_base_stat+spe_iv+(spe_ev//4))/100)*level)+5*1
            spe_stat = math.floor(spe_stat)
        elif nature == "jolly":
            hp_stat = (((2*hp_base_stat+hp_iv+(hp_ev//4) +100) / 100)*level)+10
            hp_stat = math.floor(hp_stat)
            atk_stat = ((((2*atk_base_stat+atk_iv+(atk_ev//4))/100)*level)+5)*1
            atk_stat = math.floor(atk_stat)
            def_stat = (((2*def_base_stat+def_iv+(def_ev//4))/100)*level)+5*1
            def_stat = math.floor(def_stat)
            spa_stat = (((2*spa_base_stat+spa_iv+(spa_ev//4))/100)*level)+5*0.9
            spa_stat = math.floor(spa_stat)
            spd_stat = (((2*spd_base_stat+spd_iv+(spd_ev//4))/100)*level)+5*1
            spd_stat = math.floor(spd_stat)
            spe_stat = (((2*spe_base_stat+spe_iv+(spe_ev//4))/100)*level)+5*1.1
            spe_stat = math.floor(spe_stat)
        elif nature == "naive":
            hp_stat = (((2*hp_base_stat+hp_iv+(hp_ev//4) +100) / 100)*level)+10
            hp_stat = math.floor(hp_stat)
            atk_stat = ((((2*atk_base_stat+atk_iv+(atk_ev//4))/100)*level)+5)*1
            atk_stat = math.floor(atk_stat)
            def_stat = (((2*def_base_stat+def_iv+(def_ev//4))/100)*level)+5*1
            def_stat = math.floor(def_stat)
            spa_stat = (((2*spa_base_stat+spa_iv+(spa_ev//4))/100)*level)+5*1
            spa_stat = math.floor(spa_stat)
            spd_stat = (((2*spd_base_stat+spd_iv+(spd_ev//4))/100)*level)+5*0.9
            spd_stat = math.floor(spd_stat)
            spe_stat = (((2*spe_base_stat+spe_iv+(spe_ev//4))/100)*level)+5*1.1
            spe_stat = math.floor(spe_stat)
        elif nature == "modest":
            hp_stat = (((2*hp_base_stat+hp_iv+(hp_ev//4) +100) / 100)*level)+10
            hp_stat = math.floor(hp_stat)
            atk_stat = ((((2*atk_base_stat+atk_iv+(atk_ev//4))/100)*level)+5)*0.9
            atk_stat = math.floor(atk_stat)
            def_stat = (((2*def_base_stat+def_iv+(def_ev//4))/100)*level)+5*1
            def_stat = math.floor(def_stat)
            spa_stat = (((2*spa_base_stat+spa_iv+(spa_ev//4))/100)*level)+5*1.1
            spa_stat = math.floor(spa_stat)
            spd_stat = (((2*spd_base_stat+spd_iv+(spd_ev//4))/100)*level)+5*1
            spd_stat = math.floor(spd_stat)
            spe_stat = (((2*spe_base_stat+spe_iv+(spe_ev//4))/100)*level)+5*1
            spe_stat = math.floor(spe_stat)
        elif nature == "mild":
            hp_stat = (((2*hp_base_stat+hp_iv+(hp_ev//4) +100) / 100)*level)+10
            hp_stat = math.floor(hp_stat)
            atk_stat = ((((2*atk_base_stat+atk_iv+(atk_ev//4))/100)*level)+5)*1
            atk_stat = math.floor(atk_stat)
            def_stat = (((2*def_base_stat+def_iv+(def_ev//4))/100)*level)+5*0.9
            def_stat = math.floor(def_stat)
            spa_stat = (((2*spa_base_stat+spa_iv+(spa_ev//4))/100)*level)+5*1.1
            spa_stat = math.floor(spa_stat)
            spd_stat = (((2*spd_base_stat+spd_iv+(spd_ev//4))/100)*level)+5*1
            spd_stat = math.floor(spd_stat)
            spe_stat = (((2*spe_base_stat+spe_iv+(spe_ev//4))/100)*level)+5*1
            spe_stat = math.floor(spe_stat)
        elif nature == "quiet":
            hp_stat = (((2*hp_base_stat+hp_iv+(hp_ev//4) +100) / 100)*level)+10
            hp_stat = math.floor(hp_stat)
            atk_stat = ((((2*atk_base_stat+atk_iv+(atk_ev//4))/100)*level)+5)*1
            atk_stat = math.floor(atk_stat)
            def_stat = (((2*def_base_stat+def_iv+(def_ev//4))/100)*level)+5*1
            def_stat = math.floor(def_stat)
            spa_stat = (((2*spa_base_stat+spa_iv+(spa_ev//4))/100)*level)+5*1.1
            spa_stat = math.floor(spa_stat)
            spd_stat = (((2*spd_base_stat+spd_iv+(spd_ev//4))/100)*level)+5*1
            spd_stat = math.floor(spd_stat)
            spe_stat = (((2*spe_base_stat+spe_iv+(spe_ev//4))/100)*level)+5*0.9
            spe_stat = math.floor(spe_stat)
        elif nature == "bashful":
            hp_stat = (((2*hp_base_stat+hp_iv+(hp_ev//4) +100) / 100)*level)+10
            hp_stat = math.floor(hp_stat)
            atk_stat = ((((2*atk_base_stat+atk_iv+(atk_ev//4))/100)*level)+5)*1
            atk_stat = math.floor(atk_stat)
            def_stat = (((2*def_base_stat+def_iv+(def_ev//4))/100)*level)+5*1
            def_stat = math.floor(def_stat)
            spa_stat = (((2*spa_base_stat+spa_iv+(spa_ev//4))/100)*level)+5*1
            spa_stat = math.floor(spa_stat)
            spd_stat = (((2*spd_base_stat+spd_iv+(spd_ev//4))/100)*level)+5*1
            spd_stat = math.floor(spd_stat)
            spe_stat = (((2*spe_base_stat+spe_iv+(spe_ev//4))/100)*level)+5*1
            spe_stat = math.floor(spe_stat)
        elif nature == "rash":
            hp_stat = (((2*hp_base_stat+hp_iv+(hp_ev//4) +100) / 100)*level)+10
            hp_stat = math.floor(hp_stat)
            atk_stat = ((((2*atk_base_stat+atk_iv+(atk_ev//4))/100)*level)+5)*1
            atk_stat = math.floor(atk_stat)
            def_stat = (((2*def_base_stat+def_iv+(def_ev//4))/100)*level)+5*1
            def_stat = math.floor(def_stat)
            spa_stat = (((2*spa_base_stat+spa_iv+(spa_ev//4))/100)*level)+5*1.1
            spa_stat = math.floor(spa_stat)
            spd_stat = (((2*spd_base_stat+spd_iv+(spd_ev//4))/100)*level)+5*0.9
            spd_stat = math.floor(spd_stat)
            spe_stat = (((2*spe_base_stat+spe_iv+(spe_ev//4))/100)*level)+5*1
            spe_stat = math.floor(spe_stat)
        elif nature == "calm":
            hp_stat = (((2*hp_base_stat+hp_iv+(hp_ev//4) +100) / 100)*level)+10
            hp_stat = math.floor(hp_stat)
            atk_stat = ((((2*atk_base_stat+atk_iv+(atk_ev//4))/100)*level)+5)*0.9
            atk_stat = math.floor(atk_stat)
            def_stat = (((2*def_base_stat+def_iv+(def_ev//4))/100)*level)+5*1
            def_stat = math.floor(def_stat)
            spa_stat = (((2*spa_base_stat+spa_iv+(spa_ev//4))/100)*level)+5*1
            spa_stat = math.floor(spa_stat)
            spd_stat = (((2*spd_base_stat+spd_iv+(spd_ev//4))/100)*level)+5*1.1
            spd_stat = math.floor(spd_stat)
            spe_stat = (((2*spe_base_stat+spe_iv+(spe_ev//4))/100)*level)+5*1
            spe_stat = math.floor(spe_stat)
        elif nature == "gentle":
            hp_stat = (((2*hp_base_stat+hp_iv+(hp_ev//4) +100) / 100)*level)+10
            hp_stat = math.floor(hp_stat)
            atk_stat = ((((2*atk_base_stat+atk_iv+(atk_ev//4))/100)*level)+5)*1
            atk_stat = math.floor(atk_stat)
            def_stat = (((2*def_base_stat+def_iv+(def_ev//4))/100)*level)+5*0.9
            def_stat = math.floor(def_stat)
            spa_stat = (((2*spa_base_stat+spa_iv+(spa_ev//4))/100)*level)+5*1
            spa_stat = math.floor(spa_stat)
            spd_stat = (((2*spd_base_stat+spd_iv+(spd_ev//4))/100)*level)+5*1.1
            spd_stat = math.floor(spd_stat)
            spe_stat = (((2*spe_base_stat+spe_iv+(spe_ev//4))/100)*level)+5*1
            spe_stat = math.floor(spe_stat)
        elif nature == "sassy":
            hp_stat = (((2*hp_base_stat+hp_iv+(hp_ev//4) +100) / 100)*level)+10
            hp_stat = math.floor(hp_stat)
            atk_stat = ((((2*atk_base_stat+atk_iv+(atk_ev//4))/100)*level)+5)*1
            atk_stat = math.floor(atk_stat)
            def_stat = (((2*def_base_stat+def_iv+(def_ev//4))/100)*level)+5*1
            def_stat = math.floor(def_stat)
            spa_stat = (((2*spa_base_stat+spa_iv+(spa_ev//4))/100)*level)+5*1
            spa_stat = math.floor(spa_stat)
            spd_stat = (((2*spd_base_stat+spd_iv+(spd_ev//4))/100)*level)+5*1.1
            spd_stat = math.floor(spd_stat)
            spe_stat = (((2*spe_base_stat+spe_iv+(spe_ev//4))/100)*level)+5*0.9
            spe_stat = math.floor(spe_stat)
        elif nature == "careful":
            hp_stat = (((2*hp_base_stat+hp_iv+(hp_ev//4) +100) / 100)*level)+10
            hp_stat = math.floor(hp_stat)
            atk_stat = ((((2*atk_base_stat+atk_iv+(atk_ev//4))/100)*level)+5)*1
            atk_stat = math.floor(atk_stat)
            def_stat = (((2*def_base_stat+def_iv+(def_ev//4))/100)*level)+5*1
            def_stat = math.floor(def_stat)
            spa_stat = (((2*spa_base_stat+spa_iv+(spa_ev//4))/100)*level)+5*0.9
            spa_stat = math.floor(spa_stat)
            spd_stat = (((2*spd_base_stat+spd_iv+(spd_ev//4))/100)*level)+5*1.1
            spd_stat = math.floor(spd_stat)
            spe_stat = (((2*spe_base_stat+spe_iv+(spe_ev//4))/100)*level)+5*1
            spe_stat = math.floor(spe_stat)
        elif nature == "quirky":
            hp_stat = (((2*hp_base_stat+hp_iv+(hp_ev//4) +100) / 100)*level)+10
            hp_stat = math.floor(hp_stat)
            atk_stat = ((((2*atk_base_stat+atk_iv+(atk_ev//4))/100)*level)+5)*1
            atk_stat = math.floor(atk_stat)
            def_stat = (((2*def_base_stat+def_iv+(def_ev//4))/100)*level)+5*1
            def_stat = math.floor(def_stat)
            spa_stat = (((2*spa_base_stat+spa_iv+(spa_ev//4))/100)*level)+5*1
            spa_stat = math.floor(spa_stat)
            spd_stat = (((2*spd_base_stat+spd_iv+(spd_ev//4))/100)*level)+5*1
            spd_stat = math.floor(spd_stat)
            spe_stat = (((2*spe_base_stat+spe_iv+(spe_ev//4))/100)*level)+5*1
            spe_stat = math.floor(spe_stat)
        stats = {
            "hp":hp_stat,
            "atk":atk_stat,
            "def":def_stat,
            "spa":spa_stat,
            "spd":spd_stat,
            "spe":spe_stat,
        }
        return stats

# Function to get readable time
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

# Command handler: /ping
@app.on(events.NewMessage(pattern="/ping"))
async def ping(event):
    user_list=await users()
    user_id=event.sender_id
    if user_id in user_list:
      start_time = time.time()
      end_time = time.time()
      ping_time = round((end_time - start_time) * 1000, 3)
      uptime = get_readable_time(int(time.time() - StartTime))
      await event.reply(f"Pong⋙ {ping_time}ms\nBot Is Online Since⋙ {uptime}")
    else:
      await event.reply("__**You are not an authorised user**__")

# Command handler: /start
@app.on(events.NewMessage(pattern="/start"))
async def start(event):
  
  await event.reply("__**Welcome to the bot\nNothing here to mention**__")


# Command handler: /register
@app.on(events.NewMessage(pattern="/register"))
#group
async def log_in(event):
   user_list = await users()
   user_id = event.sender_id
   if user_id in user_list:
      if event.is_group:
         await app.send_file(event.chat.id,file=error_image,caption="__**Try the operation again in private!**__",buttons=[
            [Button.url("Log In", "https://t.me/Pokemon_Masters_Game_Bot?start=start_chat")]
         ])
      elif event.is_private:
        
        check_whether_existing_user = await col.find_one({"user_id": user_id},{"Registration": 1})

        if check_whether_existing_user and "Registration" in check_whether_existing_user:
            print(f"User found in database: {check_whether_existing_user}")  # Log DB result
            await event.reply("__**You are already registered!**__")
        else:
            raw_user = {
                "user_id": user_id
            }
                # Inserting the user data into the database
            await col.insert_one(raw_user)
            print("User not found in database, added user")  # Log DB result
            x=await app.send_message(event.chat.id,"__**Your Raw Data has been created in the database!**__")
            await x.delete()
            x1=await app.send_file(event.chat.id,file=logo_image,caption="__**Preparing to start game**__")
            await asyncio.sleep(1.5)
            x2=await x1.edit("__**Getting Started**__")
            await asyncio.sleep(1.5)
            x3=await x2.edit("__**Getting things ready**__")
            await asyncio.sleep(1.5)
            x4=await x3.edit("__**Getting things ready just for you**__")
            await asyncio.sleep(1.5)
            x5=await x4.edit("__**Just sit back and relax everything will be done automatically\nJust for you**__")
            await asyncio.sleep(1.5)
            x6=await x5.edit("__**Retrieving necessary user data from the database**__")
            await asyncio.sleep(1.5)
            x7=await x6.edit("__**Requesting permission for creation of new user data to the server**__")
            await asyncio.sleep(1.5)
            x8=await x7.edit("__**Access approved , waiting for response from the server**__")
            await asyncio.sleep(1.5)
            x9=await x8.edit("__**Searching for your raw data in the database**__") 
            await asyncio.sleep(1.5)
            x10=await x9.edit("__**Please hold on while we are collecting new user creation credentials data from the server\nNote: This might take from few seconds to a minute or two! **__")
            y=random.randint(1,120)
            print(y)
            await asyncio.sleep(y)
            await x10.delete()
            await app.send_file(event.chat.id,file=connect_image,caption="__**Tell us more about yourself**__")
                            # Ask for trainer's name
            global msg
            msg = await event.reply("__**Tell us what you want to be called as**__",buttons=[
                [Button.inline("Note!",data="n1")]
            ])

            app.user_states[event.sender_id] = {
        "stage": "awaiting_name",
        "message_id": msg.id
    }
            

   else:
      await event.reply("__**You are not an authorised user!**__")

@app.on(events.NewMessage)
async def handle_message(event):
    # Get the user state
    user_state = app.user_states.get(event.sender_id)

    if user_state:
        # Check if the message is a reply to the tracked message
        if event.message.reply_to_msg_id == user_state["message_id"]:
            # Handle based on the current stage
            if user_state["stage"] == "awaiting_name":
                 
                # Get the user's name
                global name
                name = event.message.text
                if name.startswith('/'):
                    await event.reply("__**Invalid name exiting registration process**__")
                    await msg.delete()
                    app.user_states.pop(event.sender_id, None)
                    await col.delete_one({"user_id": event.sender_id})
                    return
                print(name)
                # Update the state to "awaiting_email"
                await msg.delete()
                global msg1
                msg1 = await event.reply("__**Kindly enter a valid email address which is not used already**__",buttons=[
                [Button.inline("Note!",data="n2")]
                ])
                user_state["stage"] = "awaiting_email"
                user_state["message_id"] = msg1.id

            elif user_state["stage"] == "awaiting_email":
                # Get the user's email
                global email
                email = event.message.text

                if not email.endswith("@gmail.com"):
                    await event.reply("__**Invalid email exiting registration process**__")
                    await msg1.delete()
                    app.user_states.pop(event.sender_id, None)
                    await col.delete_one({"user_id": event.sender_id})
                    return
                print(email)
                await msg1.delete()
                # Clear the user's state
                app.user_states.pop(event.sender_id, None)
                
                await col.update_one({"user_id": event.sender_id}, {"$set": {"name": name, "email": email}})
                m1=await event.reply("__**Saving your data to the server, please wait**__")
                r=random.randint(1,50)
                m2=await m1.edit(f"__**Saving your data to the server, please wait {r}%**__")
                await asyncio.sleep(1)
                r=random.randint(51,99)
                m3=await m2.edit(f"__**Saving your data to the server, please wait {r}%**__")
                await asyncio.sleep(1)
                m4=await m3.edit("__**Saving your data to the server, please wait %**__")
                await m4.delete()
                
                await event.respond(
        file="AgACAgUAAxkBAAIJ0WeI4nOrtEP5AzO4Evu_p0o5NkE1AAIhzjEbmE55VwSzkNv2eUTWAAgBAAMCAAN5AAceBA",
        buttons=[
            Button.inline("Previous", data="prev"),
            Button.inline("Select", data="select"),
            Button.inline("Next", data="next"),
        ]
    )

@app.on(events.NewMessage(pattern="/delete"))
#to delete all documents in the db
async def delete(event):
    await col.delete_many({})
    await event.reply("__**All documents have been deleted!**__")

@app.on(events.NewMessage(pattern="/launch"))
async def launch(event):
    if event.is_group:
        await app.send_file(event.chat.id,file=error_image,caption="__**Try the operation again in private!**__",buttons=[
            [Button.url("Log In", "https://t.me/Pokemon_Masters_Game_Bot?start=start_chat")]
         ])
    elif event.is_private:
        check_whether_existing_user = await col.find_one({"user_id": event.sender_id},{"Registration": 1})
        if check_whether_existing_user and "Registration" in check_whether_existing_user:
            check_partner=await col.find_one({"user_id": event.sender_id},{"partner": 1})
            if check_partner and "partner" in check_partner:
                r=random.randint(1,5)
                r1=random.randint(6,10)
                r2=random.randint(11,15)
                r3=random.randint(16,20)
                r4=random.randint(21,25)
                r5=random.randint(26,30)
                x=await app.send_file(event.chat.id,file=logo_image,caption=f"__**Loading necessary data!{r}%**__")
                await x.edit(f"__**Loading necessary data! {r1}%**__")
                await x.edit(f"__**Loading necessary data! {r2}%**__")
                await x.edit(f"__**Loading necessary data! {r3}%**__")
                await x.edit(f"__**Loading necessary data! {r4}%**__")
                await x.edit(f"__**Loading necessary data! {r5}%**__")
                r6=random.randint(31,35)
                r7=random.randint(36,40)
                r8=random.randint(41,45)
                r9=random.randint(46,50)
                r10=random.randint(51,55)
                await x.edit(f"__**Connecting with server {r6}%**__")
                await x.edit(f"__**Connecting with server {r7}%**__")
                await x.edit(f"__**Connecting with server {r8}%**__")
                await x.edit(f"__**Connecting with server {r9}%**__")
                await x.edit(f"__**Connecting with server {r10}%**__")
                r11=random.randint(56,60)
                r12=random.randint(61,65)
                r13=random.randint(66,70)
                r14=random.randint(71,75)
                r15=random.randint(76,80)
                await x.edit(f"__**Checking user credentials{r11}%**__")
                await x.edit(f"__**Checking user credentials{r12}%**__")
                await x.edit(f"__**Checking user credentials{r13}%**__")
                await x.edit(f"__**Checking user credentials{r14}%**__")
                await x.edit(f"__**Checking user credentials{r15}%**__")
                r16=random.randint(81,85)
                r17=random.randint(86,90)
                r18=random.randint(91,95)
                r19=random.randint(96,100)
                await x.edit(f"__**Logging in ...{r16}%**__")
                await x.edit(f"__**Logging in ...{r17}%**__")
                await x.edit(f"__**Logging in ...{r18}%**__")
                await x.edit(f"__**Logging in ...{r19}%**__")
                await x.delete()
            else:
                r=random.randint(1,5)
                r1=random.randint(6,10)
                r2=random.randint(11,15)
                r3=random.randint(16,20)
                r4=random.randint(21,25)
                r5=random.randint(26,30)
                x=await app.send_file(event.chat.id,file=logo_image,caption=f"__**Loading necessary data!{r}%**__")
                await x.edit(f"__**Loading necessary data! {r1}%**__")
                await x.edit(f"__**Loading necessary data! {r2}%**__")
                await x.edit(f"__**Loading necessary data! {r3}%**__")
                await x.edit(f"__**Loading necessary data! {r4}%**__")
                await x.edit(f"__**Loading necessary data! {r5}%**__")
                r6=random.randint(31,35)
                r7=random.randint(36,40)
                r8=random.randint(41,45)
                r9=random.randint(46,50)
                r10=random.randint(51,55)
                await x.edit(f"__**Connecting with server {r6}%**__")
                await x.edit(f"__**Connecting with server {r7}%**__")
                await x.edit(f"__**Connecting with server {r8}%**__")
                await x.edit(f"__**Connecting with server {r9}%**__")
                await x.edit(f"__**Connecting with server {r10}%**__")
                r11=random.randint(56,60)
                r12=random.randint(61,65)
                r13=random.randint(66,70)
                r14=random.randint(71,75)
                r15=random.randint(76,80)
                await x.edit(f"__**Checking user credentials{r11}%**__")
                await x.edit(f"__**Checking user credentials{r12}%**__")
                await x.edit(f"__**Checking user credentials{r13}%**__")
                await x.edit(f"__**Checking user credentials{r14}%**__")
                await x.edit(f"__**Checking user credentials{r15}%**__")
                r16=random.randint(81,85)
                r17=random.randint(86,90)
                r18=random.randint(91,95)
                r19=random.randint(96,100)
                await x.edit(f"__**Logging in ...{r16}%**__")
                await x.edit(f"__**Logging in ...{r17}%**__")
                await x.edit(f"__**Logging in ...{r18}%**__")
                await x.edit(f"__**Logging in ...{r19}%**__")
                await x.delete()
                await app.send_file(event.chat.id,file=version_image,buttons=[
                    [Button.inline("Bulbasaur",data="pb"),Button.inline("Charmander",data="pc"),Button.inline("Squirtle",data="ps")],
                    [Button.inline("Pikachu",data="pp"),Button.inline("Eevee",data="pe")],
                ])
        else:
            await app.send_message(event.chat.id,"__**No save data detected \n You may fix the problem by using /register or contact Support Team**__")

#/walk command
@app.on(events.NewMessage(pattern="/walk"))
async def walk(event):
    if event.is_group:
        user_list = await users()
        user_id = event.sender_id
        if user_id in user_list:
            await app.send_file(event.chat.id,file=error_image,caption="__**Try the operation again in private!**__",buttons=[
            [Button.url("Log In", "https://t.me/Pokemon_Masters_Game_Bot?start=start_chat")]
         ])
        else:
            await event.reply("__**You are not an authorized user**__")
    elif event.is_private:
        user_list = await users()
        user_id = event.sender_id
        if user_id in user_list:
            check_whether_existing_user = await col.find_one({"user_id": event.sender_id},{"Registration": 1})
            if check_whether_existing_user and "Registration" in check_whether_existing_user:
                user_battle[user_id] = {}
                user_battle[user_id]["walk"]="NO"
                check_partner=await col.find_one({"user_id": event.sender_id},{"partner": 1})
                if check_partner and "partner" in check_partner:
                    pokemon=await get_spawn("route_1")
                    await app.send_message(event.chat.id,pokemon,buttons=[Button.inline("Catch",data="catch"),Button.inline("Pokédex")])
                else:
                    await event.reply("__**Error detected!\nContact support to solve the issue**__")
            else:
                await event.reply("__**No save data has been found or failed to retrieve your user data**__")
        else:
            await event.reply("__**You are not an authorized user")
    


@app.on(events.CallbackQuery)
async def query_handler(event):
   if event.data==b"n1":
      await event.answer("Reply to the message with your unique name", alert=True)
   elif event.data==b"n2":
      await event.answer("Reply to the message with your email which is not registered already", alert=True)


@app.on(events.CallbackQuery)
async def character_navigation(event):
    user_id = event.sender_id
    if user_id not in current_indices:
        current_indices[user_id] = 0

    if event.data == b"prev":
        current_indices[user_id] = (current_indices[user_id] - 1) % len(characters)
        index = current_indices[user_id]
        global ch
        ch = await event.edit(
            file=characters[index]["url"],
            buttons=[
                Button.inline("Previous", data="prev"),
                Button.inline("Select", data="select"),
                Button.inline("Next", data="next"),
            ],
        )
    elif event.data == b"next":
        current_indices[user_id] = (current_indices[user_id] + 1) % len(characters)
        index = current_indices[user_id]
        ch = await event.edit(
            file=characters[index]["url"],
            buttons=[
                Button.inline("Previous", data="prev"),
                Button.inline("Select", data="select"),
                Button.inline("Next", data="next"),
            ],
        )
    elif event.data == b"select":
        index = current_indices[user_id]
        selected_character = characters[index]["name"]
        await save_to_db(user_id, selected_character)
        message = await event.get_message()
        await message.delete()
        k = await app.send_message(
            user_id, "__**Collecting your raw information from the bot's temporary cache**__"
        )
        await asyncio.sleep(2)
        k1 = await k.edit("__**Gathering your raw data**__")
        await asyncio.sleep(2)
        k2 = await k1.edit("__**Transfering your data to the server**__")
        await asyncio.sleep(2)
        k3 = await k2.edit("__**Registering new user by creating user save data**__")
        await asyncio.sleep(2)
        k4 = await k3.edit(
            "__**Creating personalised user cache with the server!\nPlease hold on!\nNote: This process might take from few seconds to a minute or two!**__"
        )
        r = random.randint(1, 120)
        await asyncio.sleep(r)
        k5 = await k4.edit("__**Personal save data has been created!\nUse /launch to launch the game!**__")
    elif event.data == b"pb":
        await event.delete()
        api_url = "https://nintendropokemonremainingapi.onrender.com/get-data?partner=partner-bulbasaur"
        pokemon_url = "https://pokeapi.co/api/v2/pokemon/bulbasaur/"
        bulbasaur = PartnerPokemon(api_url, pokemon_url)
        name = bulbasaur.get_name()
        id = bulbasaur.get_id()
        pokemon_id = bulbasaur.generate_pokemon_id()
        type = bulbasaur.get_type()
        type_data = type.split(" ")
        type1 = type_data[0]
        type2 = type_data[1] if len(type_data) > 1 else None
        formatted_abilities = bulbasaur.extract_abilities()
        category = bulbasaur.get_category()
        description = bulbasaur.get_description()
        nature = bulbasaur.get_nature()
        iv = bulbasaur.get_ivs()
        ev = bulbasaur.get_evs()
        moves = bulbasaur.get_moves()
        stats = bulbasaur.get_stats()
        data = {
            "Pokemon": {
                "Bulbasaur": {
                    "name": "Bulbasaur",
                    "id": id,
                    "pokemon_id": pokemon_id,
                    "type1": type1,
                    "type2": type2,
                    "ability": formatted_abilities,
                    "category": category,
                    "description": description,
                    "nature": nature,
                    "iv": iv,
                    "ev": ev,
                    "moves": moves,
                    "stats": stats,
                }
            }
        }
        await col.update_one({"user_id": user_id}, {"$set": data})
        await col.update_one({"user_id": user_id}, {"$set": {"partner": "bulbasaur"}})
        await event.respond(
            f"{name}\n{id}\n{type}\n{formatted_abilities}\n{category}\n{description}\n{nature}\n{iv}\n{ev}\n{moves}\n{stats}"
        )
        video_message = await app.get_messages(PRIVATE_GROUP_ID, ids=VIDEO_MESSAGE_ID)
        await app.send_message(
            event.sender_id, video_message, buttons=[Button.inline("----->", data="n2")]
        )
    elif event.data == b"pc":
        await event.delete()
        api_url = "https://nintendropokemonremainingapi.onrender.com/get-data?partner=partner-charmander"
        pokemon_url = "https://pokeapi.co/api/v2/pokemon/charmander/"
        charmander = PartnerPokemon(api_url, pokemon_url)
        name = charmander.get_name()
        id = charmander.get_id()
        pokemon_id = charmander.generate_pokemon_id()
        type = charmander.get_type()
        type_data = type.split(" ")
        type1 = type_data[0]
        type2 = type_data[1] if len(type_data) > 1 else None
        formatted_abilities = charmander.extract_abilities()
        category = charmander.get_category()
        description = charmander.get_description()
        nature = charmander.get_nature()
        iv = charmander.get_ivs()
        ev = charmander.get_evs()
        moves = charmander.get_moves()
        stats = charmander.get_stats()
        data = {
            "Pokemon": {
                "Charmander": {
                    "name": "Charmander",
                    "id": id,
                    "pokemon_id": pokemon_id,
                    "type1": type1,
                    "type2": type2,
                    "ability": formatted_abilities,
                    "category": category,
                    "description": description,
                    "nature": nature,
                    "iv": iv,
                    "ev": ev,
                    "moves": moves,
                    "stats": stats,
                }
            }
        }
        await col.update_one({"user_id": user_id}, {"$set": data})
        await col.update_one({"user_id": user_id}, {"$set": {"partner": "charmander"}})
        await event.respond(
            f"{name}\n{id}\n{type}\n{formatted_abilities}\n{category}\n{description}\n{nature}\n{iv}\n{ev}\n{moves}\n{stats}"
        )
        video_message = await app.get_messages(PRIVATE_GROUP_ID, ids=VIDEO_MESSAGE_ID)
        await app.send_message(
            event.sender_id, video_message, buttons=[Button.inline("----->", data="n2")]
        )
    elif event.data == b"ps":
        await event.delete()
        api_url = "https://nintendropokemonremainingapi.onrender.com/get-data?partner=partner-squirtle"
        pokemon_url = "https://pokeapi.co/api/v2/pokemon/squirtle/"
        squirtle = PartnerPokemon(api_url, pokemon_url)
        name = squirtle.get_name()
        id = squirtle.get_id()
        pokemon_id = squirtle.generate_pokemon_id()
        type = squirtle.get_type()
        type_data = type.split(" ")
        type1 = type_data[0]
        type2 = type_data[1] if len(type_data) > 1 else None
        formatted_abilities = squirtle.extract_abilities()
        category = squirtle.get_category()
        description = squirtle.get_description()
        nature = squirtle.get_nature()
        iv = squirtle.get_ivs()
        ev = squirtle.get_evs()
        moves = squirtle.get_moves()
        stats = squirtle.get_stats()
        data = {
            "Pokemon": {
                "Squirtle": {
                    "name": "Squirtle",
                    "id": id,
                    "pokemon_id": pokemon_id,
                    "type1": type1,
                    "type2": type2,
                    "ability": formatted_abilities,
                    "category": category,
                    "description": description,
                    "nature": nature,
                    "iv": iv,
                    "ev": ev,
                    "moves": moves,
                    "stats": stats,
                }
            }
        }
        await col.update_one({"user_id": user_id}, {"$set": data})
        await col.update_one({"user_id": user_id}, {"$set": {"partner": "squirtle"}})
        await event.respond(
            f"{name}\n{id}\n{type}\n{formatted_abilities}\n{category}\n{description}\n{nature}\n{iv}\n{ev}\n{moves}\n{stats}"
        )
        video_message = await app.get_messages(PRIVATE_GROUP_ID, ids=VIDEO_MESSAGE_ID)
        await app.send_message(
            event.sender_id, video_message, buttons=[Button.inline("----->", data="n2")]
        )

    elif event.data == b"pp":
        await event.delete()
        api_url = "https://nintendropokemonremainingapi.onrender.com/get-data?partner=partner-pikachu"
        pokemon_url = "https://pokeapi.co/api/v2/pokemon/pikachu/"
        pikachu = PartnerPokemon(api_url, pokemon_url)
        name = pikachu.get_name()
        id = pikachu.get_id()
        pokemon_id = pikachu.generate_pokemon_id()
        type = pikachu.get_type()
        type_data = type.split(" ")
        type1 = type_data[0]
        type2 = type_data[1] if len(type_data) > 1 else None
        formatted_abilities = pikachu.extract_abilities()
        category = pikachu.get_category()
        description = pikachu.get_description()
        nature = pikachu.get_nature()
        iv = pikachu.get_ivs()
        ev = pikachu.get_evs()
        moves = pikachu.get_moves()
        stats = pikachu.get_stats()
        data = {
            "Pokemon": {
                "Pikachu": {
                    "name": "Pikachu",
                    "id": id,
                    "pokemon_id": pokemon_id,
                    "type1": type1,
                    "type2": type2,
                    "ability": formatted_abilities,
                    "category": category,
                    "description": description,
                    "nature": nature,
                    "iv": iv,
                    "ev": ev,
                    "moves": moves,
                    "stats": stats,
                }
            }
        }
        await col.update_one({"user_id": user_id}, {"$set": data})
        await col.update_one({"user_id": user_id}, {"$set": {"partner": "pikachu"}})
        await event.respond(
            f"{name}\n{id}\n{type}\n{formatted_abilities}\n{category}\n{description}\n{nature}\n{iv}\n{ev}\n{moves}\n{stats}"
        )
        video_message = await app.get_messages(PRIVATE_GROUP_ID, ids=VIDEO_MESSAGE_ID)
        await app.send_message(
            event.sender_id, video_message, buttons=[Button.inline("----->", data="n2")]
        )

    elif event.data == b"pe":
        await event.delete()
        api_url = "https://nintendropokemonremainingapi.onrender.com/get-data?partner=partner-eevee"
        pokemon_url = "https://pokeapi.co/api/v2/pokemon/eevee/"
        eevee = PartnerPokemon(api_url, pokemon_url)
        name = eevee.get_name()
        id = eevee.get_id()
        pokemon_id = eevee.generate_pokemon_id()
        type = eevee.get_type()
        type_data = type.split(" ")
        type1 = type_data[0]
        type2 = type_data[1] if len(type_data) > 1 else None
        formatted_abilities = eevee.extract_abilities()
        category = eevee.get_category()
        description = eevee.get_description()
        nature = eevee.get_nature()
        iv = eevee.get_ivs()
        ev = eevee.get_evs()
        moves = eevee.get_moves()
        stats = eevee.get_stats()
        data = {
            "Pokemon": {
                "Eevee": {
                    "name": "Eevee",
                    "id": id,
                    "pokemon_id": pokemon_id,
                    "type1": type1,
                    "type2": type2,
                    "ability": formatted_abilities,
                    "category": category,
                    "description": description,
                    "nature": nature,
                    "iv": iv,
                    "ev": ev,
                    "moves": moves,
                    "stats": stats,
                }
            }
        }
        await col.update_one({"user_id": user_id}, {"$set": data})
        await col.update_one({"user_id": user_id}, {"$set": {"partner": "eevee"}})
        await event.respond(
            f"{name}\n{id}\n{type}\n{formatted_abilities}\n{category}\n{description}\n{nature}\n{iv}\n{ev}\n{moves}\n{stats}"
        )
        video_message = await app.get_messages(PRIVATE_GROUP_ID, ids=VIDEO_MESSAGE_ID)
        await app.send_message(
            event.sender_id, video_message, buttons=[Button.inline("----->", data="n2")]
        )
    elif event.data == b"n2":
        await event.delete()
        await app.send_message(event.sender_id, "TEXT YET TO BE ADDED")
        pokemon = await col.find_one({"user_id": user_id}, {"Pokemon": {"Pikachu": {"name": 1}}})
        x_id = await col.find_one(
            {"user_id": user_id}, {"Pokemon": {"Pikachu": {"pokemon_id": 1}}}
        )
        col.update_one(
            {"user_id": user_id},  # Match the user by ID
            {"$set": {"party": {"name": pokemon, "p_id": x_id}}},
        )
        n = await col.find_one({"user_id": user_id}, {"party": 1})
    elif event.data == b"catch":
        user_id = event.sender_id
        # Fetch user's partner pokemon data
        user_data = await col.find_one({"user_id": user_id})
        partner_pokemon_data = get_partner_pokemon_data(user_data)
        partner_hp = (
            int(partner_pokemon_data["stats"]["hp"])
            if partner_pokemon_data and "stats" in partner_pokemon_data
            else int("0")
        )
        partner_moves = partner_pokemon_data.get("moves", {})

        # fetch the wild pokemon name, level
        message = await event.get_message()  # Use get_message() to get the message object
        message_text = message.text
        parts = message_text.split("wild ", 1)
        if len(parts) > 1:
            parts1 = parts[1].split(" (Level ", 1)
        else:
            return

        wild_pokemon_name = parts1[0].capitalize()
        level = int(parts1[1][:-1])
        wild_pokemon_details = await get_wild_pokemon_details(
            wild_pokemon_name.lower(), level
        )
        wild_hp = int(wild_pokemon_details["hp"]) if wild_pokemon_details else int("0")
        partner_cur_hp = int(partner_hp)
        wild_cur_hp = int(wild_hp)
        user_battle[user_id] = {}
        user_battle[user_id]["wild_hp"] = int(wild_hp)
        user_battle[user_id]["wild_cur_hp"] = int(wild_hp)
        user_battle[user_id]["user_hp"] = int(partner_hp)
        user_battle[user_id]["user_cur_hp"] = int(partner_hp)
        user_battle[user_id]["turn"] = int(1)
        

        parthp = hp_bar(partner_cur_hp,partner_hp)
        wihp = hp_bar(wild_cur_hp,wild_hp)

        move_buttons = [
            Button.inline(move['move'], data=f"hunt_{user_id}_{move['move']}_t")
            for move in partner_moves
        ]

        # Create the message text
        message_text = (
            f"Battle begins!! \n Turn : 1 \n \n {wild_pokemon_name}'s HP:\n {wihp}\n\n"
            f"{user_data.get('partner').capitalize()}'s HP:\n {parthp}\n\n"
            f"Choose a move from below:\n"
        )

        new_buttons = [
        Button.inline("Pokeball", data=f"hunt_{user_id}_Pokeball"),
        Button.inline("Run", data=f"hunt_{user_id}_Run_t"),
        Button.inline("Switch", data=f"hunt_{user_id}_Switch_t"),
        ]

        all_buttons = [move_buttons[i : i + 2] for i in range(0, len(move_buttons), 2)] + [new_buttons]

        await event.edit(
            message_text, buttons=all_buttons
        )
    elif str(event.data).startswith("b'hunt"):
        sp = str(event.data).split("_")
        user_id = sp[1]
        if str(sp[2]) in poke_moves:
            m = sp[2].replace(" ","_")
            response = requests.get(f"https://nintendromoveapi.onrender.com/move_data/{m}")
            
            move_data = response.json()
            power =move_data["Move Data"]["Power"]
            accuracy = move_data["Move Data"]["Accuracy"]
            if power == "-":
                power = 0
            else:
                power = int(power)
            await event.answer(f"power: {power} \n Accuracy: {accuracy}", alert=True)
    else:
        await event.answer(f"{event.data}", alert=True)
async def get_wild_pokemon_details(pokemon_name, level):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/")
    if response.status_code == 200:
        pokemon_data = response.json()
        base_hp = pokemon_data['stats'][0]['base_stat']
        hp = math.floor((((2 * base_hp + 0 + 0 // 4) * level) / 100) + level + 10)
        
        return {"hp": hp}
    else:
        return None



async def save_to_db(user_id, selected_character):
    # Ensure col is your MongoDB collection instance
    col.update_one(
        {"user_id": user_id},  # Match the user by ID
        {"$set": {"selected_character": selected_character,"Registration":"done","active_user_id":user_id}}
    )


async def main():
    try:
        await app.start(bot_token=bot_token)
        print("Bot started")
        await app.run_until_disconnected()
    except Exception as e:
        print(f"Bot sttoped error \n {e}")
    finally:
        await app.disconnect()

if __name__ == "__main__":
    asyncio.run(main())