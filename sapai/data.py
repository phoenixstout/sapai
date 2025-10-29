"""


MIT License

Copyright (c) 2021 Ben Coveney

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

"""

Please note that these effects are from VERSION 180??? 10/28/25


"""

# %%
data = {
    "pets": {
        # Tier 1
        "pet-ant": {
            "name": "Ant",
            "id": "pet-ant",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐜",
            },
            "tier": 1,
            "baseAttack": 2,
            "baseHealth": 2,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Faint: Give a random friend +1/+1",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "target": {"kind": "RandomFriend", "n": 1},
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "Faint: Give a random friend +2/+2",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "target": {"kind": "RandomFriend", "n": 1},
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "Faint: Give a random friend +3/+3",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 3,
                    "healthAmount": 3,
                    "target": {"kind": "RandomFriend", "n": 1},
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
            ],
        },
        "pet-beaver": {
            "name": "Beaver",
            "id": "pet-beaver",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦫",
            },
            "tier": 1,
            "baseAttack": 3,
            "baseHealth": 2,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Sell: Give two random friends +1 attack",
                "trigger": "Sell",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 1,
                    "target": {"kind": "RandomFriend", "n": 2},
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "Sell: Give two random friends +2 attack",
                "trigger": "Sell",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 2,
                    "target": {"kind": "RandomFriend", "n": 2},
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "Sell: Give two random friends +3 attack",
                "trigger": "Sell",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 3,
                    "target": {"kind": "RandomFriend", "n": 2},
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
            ],
        },
        "pet-beetle": {
            "name": "Beetle",
            "id": "pet-beetle",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🪲",
            },
            "tier": 1,
            "baseAttack": 2,
            "baseHealth": 3,
            "packs": ["ExpansionPack1"],
            "level1Ability": {
                "description": "Eat shop food: Give shop animals +1 health",
                "trigger": "EatsShopFood",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "healthAmount": 1,
                    "target": {"kind": "EachShopAnimal", "includingFuture": False},
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "Eat shop food: Give shop animals +2 health",
                "trigger": "EatsShopFood",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "healthAmount": 2,
                    "target": {"kind": "EachShopAnimal", "includingFuture": False},
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "Eat shop food: Give shop animals +3 health",
                "trigger": "EatsShopFood",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "healthAmount": 3,
                    "target": {"kind": "EachShopAnimal", "includingFuture": False},
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {"ExpansionPack1": 0.2976680384087793},
                    "perSlot": {"ExpansionPack1": 0.1111111111111111},
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {"ExpansionPack1": 0.2976680384087793},
                    "perSlot": {"ExpansionPack1": 0.1111111111111111},
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {"ExpansionPack1": 0.14973028138212574},
                    "perSlot": {"ExpansionPack1": 0.05263157894736842},
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {"ExpansionPack1": 0.14973028138212574},
                    "perSlot": {"ExpansionPack1": 0.05263157894736842},
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {"ExpansionPack1": 0.12681358024691358},
                    "perSlot": {"ExpansionPack1": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {"ExpansionPack1": 0.12681358024691358},
                    "perSlot": {"ExpansionPack1": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"ExpansionPack1": 0.08328505725105906},
                    "perSlot": {"ExpansionPack1": 0.017241379310344827},
                },
            ],
        },
        "pet-bluebird": {
            "name": "Bluebird",
            "id": "pet-bluebird",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐦",
            },
            "tier": 1,
            "baseAttack": 2,
            "baseHealth": 1,
            "packs": ["ExpansionPack1"],
            "level1Ability": {
                "description": "End turn: Give left-most friend +1 attack",
                "trigger": "EndOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 1,
                    "target": {"kind": "LeftMostFriend"},
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "End turn: Give left-most friend +2 attack",
                "trigger": "EndOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 2,
                    "target": {"kind": "LeftMostFriend"},
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "End turn: Give left-most friend +3 attack",
                "trigger": "EndOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 3,
                    "target": {"kind": "LeftMostFriend"},
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {"ExpansionPack1": 0.2976680384087793},
                    "perSlot": {"ExpansionPack1": 0.1111111111111111},
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {"ExpansionPack1": 0.2976680384087793},
                    "perSlot": {"ExpansionPack1": 0.1111111111111111},
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {"ExpansionPack1": 0.14973028138212574},
                    "perSlot": {"ExpansionPack1": 0.05263157894736842},
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {"ExpansionPack1": 0.14973028138212574},
                    "perSlot": {"ExpansionPack1": 0.05263157894736842},
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {"ExpansionPack1": 0.12681358024691358},
                    "perSlot": {"ExpansionPack1": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {"ExpansionPack1": 0.12681358024691358},
                    "perSlot": {"ExpansionPack1": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"ExpansionPack1": 0.08328505725105906},
                    "perSlot": {"ExpansionPack1": 0.017241379310344827},
                },
            ],
        },
        "pet-cricket": {
            "name": "Cricket",
            "id": "pet-cricket",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦗",
            },
            "tier": 1,
            "baseAttack": 1,
            "baseHealth": 3,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Faint: Summon a 1/1 Cricket",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-zombie-cricket",
                    "withAttack": 1,
                    "withHealth": 1,
                    "team": "Friendly",
                },
            },
            "level2Ability": {
                "description": "Faint: Summon a 2/2 Cricket",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-zombie-cricket",
                    "withAttack": 2,
                    "withHealth": 2,
                    "team": "Friendly",
                },
            },
            "level3Ability": {
                "description": "Faint: Summon a 3/3 Cricket",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-zombie-cricket",
                    "withAttack": 3,
                    "withHealth": 3,
                    "team": "Friendly",
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
            ],
        },
        "pet-duck": {
            "name": "Duck",
            "id": "pet-duck",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦆",
            },
            "tier": 1,
            "baseAttack": 2,
            "baseHealth": 2,
            "packs": ["StandardPack"],
            "level1Ability": {
                "description": "Sell: Give shop animals +1 Health",
                "trigger": "Sell",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "EachShopAnimal", "includingFuture": False},
                    "healthAmount": 1,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "Sell: Give shop animals +2 Health",
                "trigger": "Sell",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "EachShopAnimal", "includingFuture": False},
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "Sell: Give shop animals +3 Health",
                "trigger": "Sell",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "EachShopAnimal", "includingFuture": False},
                    "healthAmount": 3,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {"StandardPack": 0.2976680384087793},
                    "perSlot": {"StandardPack": 0.1111111111111111},
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {"StandardPack": 0.2976680384087793},
                    "perSlot": {"StandardPack": 0.1111111111111111},
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {"StandardPack": 0.14973028138212574},
                    "perSlot": {"StandardPack": 0.05263157894736842},
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {"StandardPack": 0.14973028138212574},
                    "perSlot": {"StandardPack": 0.05263157894736842},
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {"StandardPack": 0.12681358024691358},
                    "perSlot": {"StandardPack": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {"StandardPack": 0.12681358024691358},
                    "perSlot": {"StandardPack": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"StandardPack": 0.08328505725105906},
                    "perSlot": {"StandardPack": 0.017241379310344827},
                },
            ],
        },
        "pet-fish": {
            "name": "Fish",
            "id": "pet-fish",
            "image": {
                "source": "fxemoji",
                "commit": "270af343bee346d8221f87806d2b1eee0438431a",
                "name": "fish",
                "unicodeCodePoint": "🐟",
            },
            "tier": 1,
            "baseAttack": 2,
            "baseHealth": 3,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Level-up: Give two friends +1/+1",
                "trigger": "LevelUp",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "RandomFriend", "n": 2},
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "Level-up: Give two friends +2/+2",
                "trigger": "LevelUp",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "RandomFriend", "n": 2},
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
            ],
        },
        "pet-horse": {
            "name": "Horse",
            "id": "pet-horse",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐎",
            },
            "tier": 1,
            "baseAttack": 2,
            "baseHealth": 1,
            "packs": ["StandardPack"],
            "level1Ability": {
                "description": "Friend summoned: Give it +1 Attack until end of battle",
                "trigger": "Summoned",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "TriggeringEntity"},
                    "attackAmount": 1,
                    "untilEndOfBattle": True,
                },
            },
            "level2Ability": {
                "description": "Friend summoned: Give it +2 Attack until end of battle",
                "trigger": "Summoned",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "TriggeringEntity"},
                    "attackAmount": 2,
                    "untilEndOfBattle": True,
                },
            },
            "level3Ability": {
                "description": "Friend summoned: Give it +3 Attack until end of battle",
                "trigger": "Summoned",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "TriggeringEntity"},
                    "attackAmount": 3,
                    "untilEndOfBattle": True,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {"StandardPack": 0.2976680384087793},
                    "perSlot": {"StandardPack": 0.1111111111111111},
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {"StandardPack": 0.2976680384087793},
                    "perSlot": {"StandardPack": 0.1111111111111111},
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {"StandardPack": 0.14973028138212574},
                    "perSlot": {"StandardPack": 0.05263157894736842},
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {"StandardPack": 0.14973028138212574},
                    "perSlot": {"StandardPack": 0.05263157894736842},
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {"StandardPack": 0.12681358024691358},
                    "perSlot": {"StandardPack": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {"StandardPack": 0.12681358024691358},
                    "perSlot": {"StandardPack": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"StandardPack": 0.08328505725105906},
                    "perSlot": {"StandardPack": 0.017241379310344827},
                },
            ],
        },
        "pet-ladybug": {
            "name": "Ladybug",
            "id": "pet-ladybug",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐞",
            },
            "tier": 1,
            "baseAttack": 1,
            "baseHealth": 3,
            "packs": ["ExpansionPack1"],
            "level1Ability": {
                "description": "Buy food: Gain +1/+1 until end of battle",
                "trigger": "BuyFood",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "target": {"kind": "Self"},
                    "untilEndOfBattle": True,
                },
            },
            "level2Ability": {
                "description": "Buy food: Gain +2/+2 until end of battle",
                "trigger": "BuyFood",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "target": {"kind": "Self"},
                    "untilEndOfBattle": True,
                },
            },
            "level3Ability": {
                "description": "Buy food: Gain +3/+3 until end of battle",
                "trigger": "BuyFood",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 3,
                    "healthAmount": 3,
                    "target": {"kind": "Self"},
                    "untilEndOfBattle": True,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {"ExpansionPack1": 0.2976680384087793},
                    "perSlot": {"ExpansionPack1": 0.1111111111111111},
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {"ExpansionPack1": 0.2976680384087793},
                    "perSlot": {"ExpansionPack1": 0.1111111111111111},
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {"ExpansionPack1": 0.14973028138212574},
                    "perSlot": {"ExpansionPack1": 0.05263157894736842},
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {"ExpansionPack1": 0.14973028138212574},
                    "perSlot": {"ExpansionPack1": 0.05263157894736842},
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {"ExpansionPack1": 0.12681358024691358},
                    "perSlot": {"ExpansionPack1": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {"ExpansionPack1": 0.12681358024691358},
                    "perSlot": {"ExpansionPack1": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"ExpansionPack1": 0.08328505725105906},
                    "perSlot": {"ExpansionPack1": 0.017241379310344827},
                },
            ],
        },
        "pet-mosquito": {
            "name": "Mosquito",
            "id": "pet-mosquito",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦟",
            },
            "tier": 1,
            "baseAttack": 2,
            "baseHealth": 2,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Start of battle: Deal 1 damage to a random enemy",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "RandomEnemy", "n": 1},
                    "amount": 1,
                },
            },
            "level2Ability": {
                "description": "Start of battle: Deal 1 damage to 2 random enemies",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "RandomEnemy", "n": 2},
                    "amount": 1,
                },
            },
            "level3Ability": {
                "description": "Start of battle: Deal 1 damage to 3 random enemies",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "RandomEnemy", "n": 3},
                    "amount": 1,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
            ],
        },
        "pet-otter": {
            "name": "Otter",
            "id": "pet-otter",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦦",
            },
            "tier": 1,
            "baseAttack": 1,
            "baseHealth": 4,
            "packs": ["StandardPack"],
            "level1Ability": {
                "description": "Buy: Give one random friend +1 health",
                "trigger": "Buy",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "RandomFriend", "n": 1},
                    "healthAmount": 1,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "Buy: Give two random friends +1 health",
                "trigger": "Buy",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "RandomFriend", "n": 2},
                    "healthAmount": 1,
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "Buy: Give three random friends +1 health",
                "trigger": "Buy",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "RandomFriend", "n": 3},
                    "healthAmount": 1,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {"StandardPack": 0.2976680384087793},
                    "perSlot": {"StandardPack": 0.1111111111111111},
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {"StandardPack": 0.2976680384087793},
                    "perSlot": {"StandardPack": 0.1111111111111111},
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {"StandardPack": 0.14973028138212574},
                    "perSlot": {"StandardPack": 0.05263157894736842},
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {"StandardPack": 0.14973028138212574},
                    "perSlot": {"StandardPack": 0.05263157894736842},
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {"StandardPack": 0.12681358024691358},
                    "perSlot": {"StandardPack": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {"StandardPack": 0.12681358024691358},
                    "perSlot": {"StandardPack": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"StandardPack": 0.08328505725105906},
                    "perSlot": {"StandardPack": 0.017241379310344827},
                },
            ],
        },
        "pet-pig": {
            "name": "Pig",
            "id": "pet-pig",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐖",
            },
            "tier": 1,
            "baseAttack": 4,
            "baseHealth": 1,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Sell: Gain an extra 1 gold",
                "trigger": "Sell",
                "triggeredBy": {"kind": "Self"},
                "effect": {"kind": "GainGold", "amount": 1},
            },
            "level2Ability": {
                "description": "Sell: Gain an extra 2 gold",
                "trigger": "Sell",
                "triggeredBy": {"kind": "Self"},
                "effect": {"kind": "GainGold", "amount": 2},
            },
            "level3Ability": {
                "description": "Sell: Gain an extra 3 gold",
                "trigger": "Sell",
                "triggeredBy": {"kind": "Self"},
                "effect": {"kind": "GainGold", "amount": 3},
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
            ],
        },
        "pet-pigeon": {
            "name": "Pigeon",
            "id": "pet-pigeon",
            "image": {
                "source": "",
                "commit": "",
                "unicodeCodePoint": "",
            },
            "tier": 1,
            "baseAttack": 3,
            "baseHealth": 1,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Sell: Stock one free Bread Crumbs",
                "trigger": "Sell",
                "triggeredBy": {"kind": "Self"},
                "effect": {},  # TODO
            },
            "level2Ability": {
                "description": "Sell: Stock two free Bread Crumbs",
                "trigger": "Sell",
                "triggeredBy": {"kind": "Self"},
                "effect": {},  # TODO
            },
            "level3Ability": {
                "description": "Sell: Stock three free Bread Crumbs",
                "trigger": "Sell",
                "triggeredBy": {"kind": "Self"},
                "effect": {},  # TODO
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
            ],
        },
        "pet-sloth": {
            "name": "Sloth",
            "id": "pet-sloth",
            "notes": "Has no special ability. Is kind of lame combat-wise. But he truly believes in you!",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦥",
            },
            "tier": 1,
            "baseAttack": 1,
            "baseHealth": 1,
            "packs": ["StandardPack", "ExpansionPack1", "EasterEgg"],
        },
        # Tier 2
        "pet-bat": {
            "name": "Bat",
            "id": "pet-bat",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦇",
            },
            "tier": 2,
            "baseAttack": 1,
            "baseHealth": 2,
            "packs": ["ExpansionPack1"],
            "level1Ability": {
                "description": "Start of battle: Make 1 enemy Weak.",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ApplyStatus",
                    "status": "status-weak",
                    "target": {"kind": "NonWeakEnemy", "n": 1},
                },
            },
            "level2Ability": {
                "description": "Start of battle: Make 2 enemies Weak.",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ApplyStatus",
                    "status": "status-weak",
                    "target": {"kind": "NonWeakEnemy", "n": 2},
                },
            },
            "level3Ability": {
                "description": "Start of battle: Make 3 enemies Weak.",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ApplyStatus",
                    "status": "status-weak",
                    "target": {"kind": "NonWeakEnemy", "n": 3},
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {"ExpansionPack1": 0.14973028138212574},
                    "perSlot": {"ExpansionPack1": 0.05263157894736842},
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {"ExpansionPack1": 0.14973028138212574},
                    "perSlot": {"ExpansionPack1": 0.05263157894736842},
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {"ExpansionPack1": 0.12681358024691358},
                    "perSlot": {"ExpansionPack1": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {"ExpansionPack1": 0.12681358024691358},
                    "perSlot": {"ExpansionPack1": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"ExpansionPack1": 0.08328505725105906},
                    "perSlot": {"ExpansionPack1": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-1",
                    "perSlot": {"ExpansionPack1": 0.1},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-2",
                    "perSlot": {"ExpansionPack1": 0.1},
                },
            ],
        },
        "pet-crab": {
            "name": "Crab",
            "id": "pet-crab",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦀",
            },
            "tier": 2,
            "baseAttack": 4,
            "baseHealth": 1,
            "packs": ["StandardPack"],
            "level1Ability": {
                "description": "Start of battle: copy 25% of health from most healthy friend",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "TransferStats",
                    "copyAttack": False,
                    "copyHealth": True,
                    "from": {"kind": "HighestHealthFriend"},
                    "target": {"kind": "Self"},
                    "percentage": 25,
                },
            },
            "level2Ability": {
                "description": "Start of battle: copy 50% of health from most healthy friend",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "TransferStats",
                    "copyAttack": False,
                    "copyHealth": True,
                    "from": {"kind": "HighestHealthFriend"},
                    "target": {"kind": "Self"},
                    "percentage": 50,
                },
            },
            "level3Ability": {
                "description": "Start of battle: copy 75% of health from most healthy friend",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "TransferStats",
                    "copyAttack": False,
                    "copyHealth": True,
                    "from": {"kind": "HighestHealthFriend"},
                    "target": {"kind": "Self"},
                    "percentage": 75,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {"StandardPack": 0.14973028138212574},
                    "perSlot": {"StandardPack": 0.05263157894736842},
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {"StandardPack": 0.14973028138212574},
                    "perSlot": {"StandardPack": 0.05263157894736842},
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {"StandardPack": 0.12681358024691358},
                    "perSlot": {"StandardPack": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {"StandardPack": 0.12681358024691358},
                    "perSlot": {"StandardPack": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"StandardPack": 0.08328505725105906},
                    "perSlot": {"StandardPack": 0.017241379310344827},
                },
                {"kind": "levelup", "turn": "turn-1", "perSlot": {"StandardPack": 0.1}},
                {"kind": "levelup", "turn": "turn-2", "perSlot": {"StandardPack": 0.1}},
            ],
        },
        "pet-dromedary": {
            "name": "Dromedary",
            "id": "pet-dromedary",
            "image": {
                "source": "noto-emoji",
                "commit": "f2a4f72bffe0212c72949a22698be235269bfab5",
                "unicodeCodePoint": "🐪",
            },
            "tier": 2,
            "baseAttack": 2,
            "baseHealth": 4,
            "packs": ["ExpansionPack1"],
            "level1Ability": {
                "description": "Start of turn: Give shop animals +1/+1",
                "trigger": "StartOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "untilEndOfBattle": False,
                    "target": {"kind": "EachShopAnimal", "includingFuture": False},
                    "attackAmount": 1,
                    "healthAmount": 1,
                },
            },
            "level2Ability": {
                "description": "Start of turn: Give shop animals +2/+2",
                "trigger": "StartOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "untilEndOfBattle": False,
                    "target": {"kind": "EachShopAnimal", "includingFuture": False},
                    "attackAmount": 2,
                    "healthAmount": 2,
                },
            },
            "level3Ability": {
                "description": "Start of turn: Give shop animals +3/+3",
                "trigger": "StartOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "untilEndOfBattle": False,
                    "target": {"kind": "EachShopAnimal", "includingFuture": False},
                    "attackAmount": 3,
                    "healthAmount": 3,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {"ExpansionPack1": 0.14973028138212574},
                    "perSlot": {"ExpansionPack1": 0.05263157894736842},
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {"ExpansionPack1": 0.14973028138212574},
                    "perSlot": {"ExpansionPack1": 0.05263157894736842},
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {"ExpansionPack1": 0.12681358024691358},
                    "perSlot": {"ExpansionPack1": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {"ExpansionPack1": 0.12681358024691358},
                    "perSlot": {"ExpansionPack1": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"ExpansionPack1": 0.08328505725105906},
                    "perSlot": {"ExpansionPack1": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-1",
                    "perSlot": {"ExpansionPack1": 0.1},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-2",
                    "perSlot": {"ExpansionPack1": 0.1},
                },
            ],
        },
        "pet-flamingo": {
            "name": "Flamingo",
            "id": "pet-flamingo",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦩",
            },
            "tier": 2,
            "baseAttack": 3,
            "baseHealth": 2,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Faint: Give the two friends behind +1/+1.",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "FriendBehind", "n": 2},
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "Faint: Give the two friends behind +2/+2.",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "FriendBehind", "n": 2},
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "Faint: Give the two friends behind +3/+3.",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "FriendBehind", "n": 2},
                    "attackAmount": 3,
                    "healthAmount": 3,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-1",
                    "perSlot": {"StandardPack": 0.1, "ExpansionPack1": 0.1},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-2",
                    "perSlot": {"StandardPack": 0.1, "ExpansionPack1": 0.1},
                },
            ],
        },
        "pet-hedgehog": {
            "name": "Hedgehog",
            "id": "pet-hedgehog",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦔",
            },
            "tier": 2,
            "baseAttack": 4,
            "baseHealth": 2,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Faint: Deal 2 damage to all.",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "All"},
                    "amount": 2,
                },
            },
            "level2Ability": {
                "description": "Faint: Deal 4 damage to all.",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "All"},
                    "amount": 4,
                },
            },
            "level3Ability": {
                "description": "Faint: Deal 6 damage to all.",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "All"},
                    "amount": 6,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-1",
                    "perSlot": {"StandardPack": 0.1, "ExpansionPack1": 0.1},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-2",
                    "perSlot": {"StandardPack": 0.1, "ExpansionPack1": 0.1},
                },
            ],
        },
        "pet-kangaroo": {
            "name": "Kangaroo",
            "id": "pet-kangaroo",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦘",
            },
            "tier": 2,
            "baseAttack": 2,
            "baseHealth": 2,
            "packs": ["StandardPack"],
            "level1Ability": {
                "description": "Friend ahead attacks: Gain +1/+1",
                "trigger": "AfterAttack",
                "triggeredBy": {"kind": "FriendAhead", "n": 1},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "Friend ahead attacks: Gain +2/+2",
                "trigger": "AfterAttack",
                "triggeredBy": {"kind": "FriendAhead", "n": 1},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "Friend ahead attacks: Gain +3/+3",
                "trigger": "AfterAttack",
                "triggeredBy": {"kind": "FriendAhead", "n": 1},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 3,
                    "healthAmount": 3,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {"StandardPack": 0.12681358024691358},
                    "perSlot": {"StandardPack": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {"StandardPack": 0.12681358024691358},
                    "perSlot": {"StandardPack": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"StandardPack": 0.08328505725105906},
                    "perSlot": {"StandardPack": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {"StandardPack": 0.09090909090909091},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {"StandardPack": 0.09090909090909091},
                },
            ],
        },
        "pet-peacock": {
            "name": "Peacock",
            "id": "pet-peacock",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦚",
            },
            "tier": 2,
            "baseAttack": 2,
            "baseHealth": 5,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Hurt: Gain 3 attack.",
                "trigger": "Hurt",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 3,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "Hurt: Gain 6 attack.",
                "trigger": "Hurt",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 6,
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "Hurt: Gain 9 attack.",
                "trigger": "Hurt",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 9,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-1",
                    "perSlot": {"StandardPack": 0.1, "ExpansionPack1": 0.1},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-2",
                    "perSlot": {"StandardPack": 0.1, "ExpansionPack1": 0.1},
                },
            ],
        },
        "pet-rat": {
            "name": "Rat",
            "id": "pet-rat",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐀",
            },
            "tier": 2,
            "baseAttack": 4,
            "baseHealth": 5,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Faint: summon one 1/1 Dirty Rat for the opponent that betrays him.",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-dirty-rat",
                    "team": "Enemy",
                },
            },
            "level2Ability": {
                "description": "Faint: summon one 1/1 Dirty Rat for the opponent that betrays him.",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-dirty-rat",
                    "team": "Enemy",
                },
            },
            "level3Ability": {
                "description": "Faint: summon one 1/1 Dirty Rat for the opponent that betrays him.",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-dirty-rat",
                    "team": "Enemy",
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-1",
                    "perSlot": {"StandardPack": 0.1, "ExpansionPack1": 0.1},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-2",
                    "perSlot": {"StandardPack": 0.1, "ExpansionPack1": 0.1},
                },
            ],
        },
        "pet-shrimp": {
            "name": "Shrimp",
            "id": "pet-shrimp",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦐",
            },
            "tier": 2,
            "baseAttack": 2,
            "baseHealth": 3,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Friend sold: Give a random friend +1 Health.",
                "trigger": "Sell",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "RandomFriend", "n": 1},
                    "healthAmount": 1,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "Friend sold: Give a random friend +2 Health.",
                "trigger": "Sell",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "RandomFriend", "n": 1},
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "Friend sold: Give a random friend +3 Health.",
                "trigger": "Sell",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "RandomFriend", "n": 1},
                    "healthAmount": 3,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-1",
                    "perSlot": {"StandardPack": 0.1, "ExpansionPack1": 0.1},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-2",
                    "perSlot": {"StandardPack": 0.1, "ExpansionPack1": 0.1},
                },
            ],
        },
        "pet-snail": {
            "name": "Snail",
            "id": "pet-snail",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐌",
            },
            "tier": 2,
            "baseAttack": 2,
            "baseHealth": 2,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Buy: If you lost last battle, give 3 nearest friends ahead +1 attack",
                "trigger": "BuyAfterLoss",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "FriendAhead", "n": 3},
                    "attackAmount": 1,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "Buy: If you lost last battle, give 3 nearest friends ahead +2 attack",
                "trigger": "BuyAfterLoss",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "FriendAhead", "n": 3},
                    "attackAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "Buy: If you lost last battle, give 3 nearest friends ahead +3 attack",
                "trigger": "BuyAfterLoss",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "FriendAhead", "n": 3},
                    "attackAmount": 3,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091,
                    },
                },
            ],
        },
        "pet-spider": {
            "name": "Spider",
            "id": "pet-spider",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🕷",
            },
            "tier": 2,
            "baseAttack": 2,
            "baseHealth": 2,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Faint: Summon a level 1 tier 3 animal as a 2/2",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "SummonRandomPet",
                    "tier": 3,
                    "baseAttack": 2,
                    "baseHealth": 2,
                    "level": 1,
                },
            },
            "level2Ability": {
                "description": "Faint: Summon a level 2 tier 3 animal as a 2/2",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "SummonRandomPet",
                    "tier": 3,
                    "baseAttack": 2,
                    "baseHealth": 2,
                    "level": 2,
                },
            },
            "level3Ability": {
                "description": "Faint: Summon a level 3 tier 3 animal as a 2/2",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "SummonRandomPet",
                    "tier": 3,
                    "baseAttack": 2,
                    "baseHealth": 2,
                    "level": 3,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-1",
                    "perSlot": {"StandardPack": 0.1, "ExpansionPack1": 0.1},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-2",
                    "perSlot": {"StandardPack": 0.1, "ExpansionPack1": 0.1},
                },
            ],
        },
        "pet-swan": {
            "name": "Swan",
            "id": "pet-swan",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🦢",
            },
            "tier": 2,
            "baseAttack": 1,
            "baseHealth": 3,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Start of turn: Gain 1 gold.",
                "trigger": "StartOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {"kind": "GainGold", "amount": 1},
            },
            "level2Ability": {
                "description": "Start of turn: Gain 2 gold.",
                "trigger": "StartOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {"kind": "GainGold", "amount": 2},
            },
            "level3Ability": {
                "description": "Start of turn: Gain 3 gold.",
                "trigger": "StartOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {"kind": "GainGold", "amount": 3},
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574,
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-1",
                    "perSlot": {"StandardPack": 0.1, "ExpansionPack1": 0.1},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-2",
                    "perSlot": {"StandardPack": 0.1, "ExpansionPack1": 0.1},
                },
            ],
        },
        "pet-worm": {
            "name": "Worm",
            "id": "pet-worm",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🪱",
            },
            "tier": 2,
            "baseAttack": 1,
            "baseHealth": 4,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Start of turn stock one 2-gold Apple",
                "trigger": "StartOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "StockShop",
                    "shop": "Food",  # Not sure what this is for but it is in RefillShop for cow
                    "food": "food-apple",
                    "cost": 2,
                },
            },
            "level2Ability": {
                "description": "Start of turn stock one 2-gold Better Apple",
                "trigger": "StartOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "StockShop",
                    "shop": "Food",  # Not sure what this is for but it is in RefillShop for cow
                    "food": "food-better-apple",
                    "cost": 2,
                },
            },
            "level3Ability": {
                "description": "Start of turn stock one 2-gold Best Apple",
                "trigger": "StartOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "StockShop",
                    "shop": "Food",  # Not sure what this is for but it is in RefillShop for cow
                    "food": "food-best-apple",
                    "cost": 2,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-5",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-6",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091,
                    },
                },
            ],
        },
        "pet-tabby-cat": {
            "name": "Tabby Cat",
            "id": "pet-tabby-cat",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐈",
            },
            "tier": 2,
            "baseAttack": 5,
            "baseHealth": 3,
            "packs": ["ExpansionPack1"],
            "level1Ability": {
                "description": "Eats shop food: Give friends +1 Attack until end of battle",
                "trigger": "EatsShopFood",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "EachFriend"},
                    "attackAmount": 1,
                    "untilEndOfBattle": True,
                },
            },
            "level2Ability": {
                "description": "Eats shop food: Give friends +2 Attack until end of battle",
                "trigger": "EatsShopFood",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "EachFriend"},
                    "attackAmount": 2,
                    "untilEndOfBattle": True,
                },
            },
            "level3Ability": {
                "description": "Eats shop food: Give friends +3 Attack until end of battle",
                "trigger": "EatsShopFood",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "EachFriend"},
                    "attackAmount": 3,
                    "untilEndOfBattle": True,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {"ExpansionPack1": 0.14973028138212574},
                    "perSlot": {"ExpansionPack1": 0.05263157894736842},
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {"ExpansionPack1": 0.14973028138212574},
                    "perSlot": {"ExpansionPack1": 0.05263157894736842},
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {"ExpansionPack1": 0.12681358024691358},
                    "perSlot": {"ExpansionPack1": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {"ExpansionPack1": 0.12681358024691358},
                    "perSlot": {"ExpansionPack1": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"ExpansionPack1": 0.08328505725105906},
                    "perSlot": {"ExpansionPack1": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-1",
                    "perSlot": {"ExpansionPack1": 0.1},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-2",
                    "perSlot": {"ExpansionPack1": 0.1},
                },
            ],
        },
        # Tier 3
        "pet-badger": {
            "name": "Badger",
            "id": "pet-badger",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦡",
            },
            "tier": 3,
            "baseAttack": 6,
            "baseHealth": 3,
            "packs": ["StandardPack"],
            "level1Ability": {
                "description": "Faint: Deal 50% Attack damage to adjacent animals",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "AdjacentAnimals"},
                    "amount": {"attackDamagePercent": 50},
                },
            },
            "level2Ability": {
                "description": "Faint: Deal 100% Attack damage to adjacent animals",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "AdjacentAnimals"},
                    "amount": {"attackDamagePercent": 100},
                },
            },
            "level3Ability": {
                "description": "Faint: Deal 150% Attack damage to adjacent animals",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "AdjacentAnimals"},
                    "amount": {"attackDamagePercent": 150},
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {"StandardPack": 0.12681358024691358},
                    "perSlot": {"StandardPack": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {"StandardPack": 0.12681358024691358},
                    "perSlot": {"StandardPack": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"StandardPack": 0.08328505725105906},
                    "perSlot": {"StandardPack": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {"StandardPack": 0.09090909090909091},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {"StandardPack": 0.09090909090909091},
                },
            ],
        },
        "pet-caterpillar": {
            "name": "Caterpillar",
            "id": "pet-caterpillar",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐛",
            },
            "tier": 3,
            "baseAttack": 1,
            "baseHealth": 3,
            "packs": ["ExpansionPack1"],
            "level1Ability": {
                "description": "Start of turn: Gain 1 Experience.",
                "trigger": "StartOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "GainExperience",
                    "target": {"kind": "Self"},
                    "amount": 1,
                },
            },
            "level2Ability": {
                "description": "Start of turn: Gain 1 Experience.",
                "trigger": "StartOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "GainExperience",
                    "target": {"kind": "Self"},
                    "amount": 1,
                },
            },
            "level3Ability": {
                "description": "Start of battle: Evolve into a Butterfly, then copy stats of the strongest friend.",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "Evolve",
                    "into": "pet-butterfly",
                    "target": {"kind": "Self"},
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {"ExpansionPack1": 0.12681358024691358},
                    "perSlot": {"ExpansionPack1": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {"ExpansionPack1": 0.12681358024691358},
                    "perSlot": {"ExpansionPack1": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"ExpansionPack1": 0.08328505725105906},
                    "perSlot": {"ExpansionPack1": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {"ExpansionPack1": 0.09090909090909091},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {"ExpansionPack1": 0.09090909090909091},
                },
            ],
        },
        "pet-camel": {
            "name": "Camel",
            "id": "pet-camel",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐫",
            },
            "tier": 3,
            "baseAttack": 3,
            "baseHealth": 3,
            "packs": ["StandardPack"],
            "level1Ability": {
                "description": "Hurt: Give friend behind +1/+2",
                "trigger": "Hurt",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "FriendBehind", "n": 1},
                    "attackAmount": 1,
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "Hurt: Give friend behind +2/+4",
                "trigger": "Hurt",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "FriendBehind", "n": 1},
                    "attackAmount": 2,
                    "healthAmount": 4,
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "Hurt: Give friend behind +3/+6",
                "trigger": "Hurt",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "FriendBehind", "n": 1},
                    "attackAmount": 3,
                    "healthAmount": 6,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {"StandardPack": 0.12681358024691358},
                    "perSlot": {"StandardPack": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {"StandardPack": 0.12681358024691358},
                    "perSlot": {"StandardPack": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"StandardPack": 0.08328505725105906},
                    "perSlot": {"StandardPack": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {"StandardPack": 0.09090909090909091},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {"StandardPack": 0.09090909090909091},
                },
            ],
        },
        "pet-dodo": {
            "name": "Dodo",
            "id": "pet-dodo",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦤",
            },
            "tier": 3,
            "baseAttack": 4,
            "baseHealth": 2,
            "packs": ["StandardPack"],
            "level1Ability": {
                "description": "Start of battle: Give 50% Attack to friend ahead.",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "TransferStats",
                    "copyAttack": True,
                    "copyHealth": False,
                    "from": {"kind": "Self"},
                    "target": {"kind": "FriendAhead", "n": 1},
                    "percentage": 50,
                },
            },
            "level2Ability": {
                "description": "Start of battle: Give 100% Attack to friend ahead.",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "TransferStats",
                    "copyAttack": True,
                    "copyHealth": False,
                    "from": {"kind": "Self"},
                    "target": {"kind": "FriendAhead", "n": 1},
                    "percentage": 100,
                },
            },
            "level3Ability": {
                "description": "Start of battle: Give 150% Attack to friend ahead.",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "TransferStats",
                    "copyAttack": True,
                    "copyHealth": False,
                    "from": {"kind": "Self"},
                    "target": {"kind": "FriendAhead", "n": 1},
                    "percentage": 150,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {"StandardPack": 0.14973028138212574},
                    "perSlot": {"StandardPack": 0.05263157894736842},
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {"StandardPack": 0.14973028138212574},
                    "perSlot": {"StandardPack": 0.05263157894736842},
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {"StandardPack": 0.12681358024691358},
                    "perSlot": {"StandardPack": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {"StandardPack": 0.12681358024691358},
                    "perSlot": {"StandardPack": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"StandardPack": 0.08328505725105906},
                    "perSlot": {"StandardPack": 0.017241379310344827},
                },
                {"kind": "levelup", "turn": "turn-1", "perSlot": {"StandardPack": 0.1}},
                {"kind": "levelup", "turn": "turn-2", "perSlot": {"StandardPack": 0.1}},
            ],
        },
        "pet-dog": {
            "name": "Dog",
            "id": "pet-dog",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🐕",
            },
            "tier": 3,
            "baseAttack": 3,
            "baseHealth": 2,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Friend summoned: Gain +2 Attack and +1 Health until end of battle.",
                "trigger": "Summoned",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 2,
                    "healthAmount": 1,
                    "untilEndOfBattle": True,
                },
            },
            "level2Ability": {
                "description": "Friend summoned: Gain +4 Attack and +2 Health until end of battle.",
                "trigger": "Summoned",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 4,
                    "healthAmount": 2,
                    "untilEndOfBattle": True,
                },
            },
            "level3Ability": {
                "description": "Friend summoned: Gain +6 Attack and +3 Health until end of battle.",
                "trigger": "Summoned",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 6,
                    "healthAmount": 3,
                    "untilEndOfBattle": True,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091,
                    },
                },
            ],
        },
        "pet-dolphin": {  # TODO - Implement "triggers n times"
            "name": "Dolphin",
            "id": "pet-dolphin",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐬",
            },
            "tier": 3,
            "baseAttack": 4,
            "baseHealth": 3,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Start of battle: Deal 4 damage to the lowest health enemy",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "LowestHealthEnemy"},
                    "amount": 4,
                },
            },
            "level2Ability": {
                "description": "Start of battle: Deal 4 damage to the lowest health enemy. Triggers 2 times.",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "LowestHealthEnemy"},
                    "amount": 4,
                },
            },
            "level3Ability": {
                "description": "Start of battle: Deal 4 damage to the lowest health enemy. Triggers 3 times.",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "LowestHealthEnemy"},
                    "amount": 4,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-5",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-6",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091,
                    },
                },
            ],
        },
        "pet-elephant": {  # TODO - Implement "triggers n times"
            "name": "Elephant",
            "id": "pet-elephant",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐘",
            },
            "tier": 2,
            "baseAttack": 3,
            "baseHealth": 7,
            "packs": ["StandardPack"],
            "level1Ability": {
                "description": "After Attack: Deal 1 damage to 1 friends behind.",
                "trigger": "AfterAttack",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "FriendBehind", "n": 1},
                    "amount": 1,
                },
            },
            "level2Ability": {
                "description": "After Attack: Deal 1 damage to friend behind. Triggers twice.",
                "trigger": "AfterAttack",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "FriendBehind", "n": 1},
                    "amount": 1,
                },
            },
            "level3Ability": {
                "description": "After Attack: Deal 1 damage to friend behind. Triggers thrice.",
                "trigger": "AfterAttack",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "FriendBehind", "n": 1},
                    "amount": 1,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {"StandardPack": 0.14973028138212574},
                    "perSlot": {"StandardPack": 0.05263157894736842},
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {"StandardPack": 0.14973028138212574},
                    "perSlot": {"StandardPack": 0.05263157894736842},
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {"StandardPack": 0.12681358024691358},
                    "perSlot": {"StandardPack": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {"StandardPack": 0.12681358024691358},
                    "perSlot": {"StandardPack": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"StandardPack": 0.08328505725105906},
                    "perSlot": {"StandardPack": 0.017241379310344827},
                },
                {"kind": "levelup", "turn": "turn-1", "perSlot": {"StandardPack": 0.1}},
                {"kind": "levelup", "turn": "turn-2", "perSlot": {"StandardPack": 0.1}},
            ],
        },
        "pet-hatching-chick": {
            "name": "Hatching Chick",
            "id": "pet-hatching-chick",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐣",
            },
            "tier": 3,
            "baseAttack": 1,
            "baseHealth": 1,
            "packs": ["ExpansionPack1"],
            "level1Ability": {
                "description": "End turn: Give +5/+5 to friend ahead until end of battle.",
                "trigger": "EndOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "FriendAhead", "n": 1},
                    "attackAmount": 5,
                    "healthAmount": 5,
                    "untilEndOfBattle": True,
                },
            },
            "level2Ability": {
                "description": "End turn: Give +2/+2 to friend ahead.",
                "trigger": "EndOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "FriendAhead", "n": 1},
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "Start of turn: Give +1 Experience to friend ahead",
                "trigger": "StartOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "GainExperience",
                    "target": {"kind": "FriendAhead", "n": 1},
                    "amount": 1,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {"ExpansionPack1": 0.12681358024691358},
                    "perSlot": {"ExpansionPack1": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {"ExpansionPack1": 0.12681358024691358},
                    "perSlot": {"ExpansionPack1": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"ExpansionPack1": 0.08328505725105906},
                    "perSlot": {"ExpansionPack1": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {"ExpansionPack1": 0.09090909090909091},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {"ExpansionPack1": 0.09090909090909091},
                },
            ],
        },
        "pet-giraffe": {
            "name": "Giraffe",
            "id": "pet-giraffe",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🦒",
            },
            "tier": 3,
            "baseAttack": 1,
            "baseHealth": 2,
            "packs": ["StandardPack"],
            "level1Ability": {
                "description": "Start turn: Give friend ahead +1/+1",
                "trigger": "StartOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "FriendAhead", "n": 1},
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "Start turn: Give 2 friends ahead +1/+1",
                "trigger": "StartOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "FriendAhead", "n": 2},
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "Start turn: Give 3 friends ahead +1/+1",
                "trigger": "StartOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "FriendAhead", "n": 3},
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {"StandardPack": 0.12681358024691358},
                    "perSlot": {"StandardPack": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {"StandardPack": 0.12681358024691358},
                    "perSlot": {"StandardPack": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"StandardPack": 0.08328505725105906},
                    "perSlot": {"StandardPack": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {"StandardPack": 0.09090909090909091},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {"StandardPack": 0.09090909090909091},
                },
            ],
        },
        "pet-owl": {
            "name": "Owl",
            "id": "pet-owl",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦉",
            },
            "tier": 3,
            "baseAttack": 5,
            "baseHealth": 3,
            "packs": ["ExpansionPack1"],
            "level1Ability": {
                "description": "Sell: Give a random friend +2/+2",
                "trigger": "Sell",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "RandomFriend", "n": 1},
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "Sell: Give a random friend +2/+2",
                "trigger": "Sell",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "RandomFriend", "n": 1},
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "Sell: Give a random friend +2/+2",
                "trigger": "Sell",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "RandomFriend", "n": 1},
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {"ExpansionPack1": 0.12681358024691358},
                    "perSlot": {"ExpansionPack1": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {"ExpansionPack1": 0.12681358024691358},
                    "perSlot": {"ExpansionPack1": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"ExpansionPack1": 0.08328505725105906},
                    "perSlot": {"ExpansionPack1": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {"ExpansionPack1": 0.09090909090909091},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {"ExpansionPack1": 0.09090909090909091},
                },
            ],
        },
        "pet-ox": {
            "name": "Ox",
            "id": "pet-ox",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐂",
            },
            "tier": 3,
            "baseAttack": 1,
            "baseHealth": 3,
            "packs": ["StandardPack"],
            "level1Ability": {
                "description": "Friend ahead attacks: Gain Melon Armor and +1 attack. Works 1 time per turn.",
                "trigger": "Faint",
                "triggeredBy": {"kind": "FriendAhead", "n": 1},
                "effect": {
                    "kind": "AllOf",
                    "effects": [
                        {
                            "kind": "ApplyStatus",
                            "status": "status-melon-armor",
                            "target": {"kind": "Self"},
                        },
                        {
                            "kind": "ModifyStats",
                            "target": {"kind": "Self"},
                            "attackAmount": 1,
                            "untilEndOfBattle": False,
                        },
                    ],
                },
                "maxTriggers": 1,
            },
            "level2Ability": {
                "description": "Friend ahead attacks: Gain Melon Armor and +1 attack. Works 2 times per turn.",
                "trigger": "Faint",
                "triggeredBy": {"kind": "FriendAhead", "n": 1},
                "effect": {
                    "kind": "AllOf",
                    "effects": [
                        {
                            "kind": "ApplyStatus",
                            "status": "status-melon-armor",
                            "target": {"kind": "Self"},
                        },
                        {
                            "kind": "ModifyStats",
                            "target": {"kind": "Self"},
                            "attackAmount": 1,
                            "untilEndOfBattle": False,
                        },
                    ],
                },
                "maxTriggers": 2,
            },
            "level3Ability": {
                "description": "Friend ahead attacks: Gain Melon Armor and +1 attack. Works 3 times per turn.",
                "trigger": "Faint",
                "triggeredBy": {"kind": "FriendAhead", "n": 1},
                "effect": {
                    "kind": "AllOf",
                    "effects": [
                        {
                            "kind": "ApplyStatus",
                            "status": "status-melon-armor",
                            "target": {"kind": "Self"},
                        },
                        {
                            "kind": "ModifyStats",
                            "target": {"kind": "Self"},
                            "attackAmount": 1,
                            "untilEndOfBattle": False,
                        },
                    ],
                },
                "maxTriggers": 3,
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {"StandardPack": 0.12681358024691358},
                    "perSlot": {"StandardPack": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {"StandardPack": 0.12681358024691358},
                    "perSlot": {"StandardPack": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"StandardPack": 0.08328505725105906},
                    "perSlot": {"StandardPack": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {"StandardPack": 0.09090909090909091},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {"StandardPack": 0.09090909090909091},
                },
            ],
        },
        "pet-puppy": {
            "name": "Puppy",
            "id": "pet-puppy",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐕",
            },
            "tier": 3,
            "baseAttack": 1,
            "baseHealth": 1,
            "packs": ["ExpansionPack1"],
            "level1Ability": {
                "description": "End turn: If you have 3 or more gold, gain +2/+2",
                "trigger": "EndOfTurnWith3PlusGold",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "End turn: If you have 3 or more gold, gain +4/+4",
                "trigger": "EndOfTurnWith3PlusGold",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 4,
                    "healthAmount": 4,
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "End turn: If you have 3 or more gold, gain +6/+6",
                "trigger": "EndOfTurnWith3PlusGold",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 6,
                    "healthAmount": 6,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {"ExpansionPack1": 0.12681358024691358},
                    "perSlot": {"ExpansionPack1": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {"ExpansionPack1": 0.12681358024691358},
                    "perSlot": {"ExpansionPack1": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"ExpansionPack1": 0.08328505725105906},
                    "perSlot": {"ExpansionPack1": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {"ExpansionPack1": 0.09090909090909091},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {"ExpansionPack1": 0.09090909090909091},
                },
            ],
        },
        "pet-rabbit": {
            "name": "Rabbit",
            "id": "pet-rabbit",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐇",
            },
            "tier": 3,
            "baseAttack": 1,
            "baseHealth": 2,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Pet eats shop food: Give it +1 Health. Works 3 times per turn.",
                "trigger": "EatsShopFood",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "TriggeringEntity"},
                    "healthAmount": 1,
                    "untilEndOfBattle": False,
                },
                "maxTriggers": 3,
            },
            "level2Ability": {
                "description": "Pet eats shop food: Give it +2 Health. Works 3 times per turn.",
                "trigger": "EatsShopFood",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "TriggeringEntity"},
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
                "maxTriggers": 3,
            },
            "level3Ability": {
                "description": "Pet eats shop food: Give it +3 Health. Works 3 times per turn.",
                "trigger": "EatsShopFood",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "TriggeringEntity"},
                    "healthAmount": 3,
                    "untilEndOfBattle": False,
                },
                "maxTriggers": 3,
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091,
                    },
                },
            ],
        },
        "pet-sheep": {
            "name": "Sheep",
            "id": "pet-sheep",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐑",
            },
            "tier": 3,
            "baseAttack": 2,
            "baseHealth": 2,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Faint: Summon two 2/2 Rams",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-ram",
                    "withAttack": 2,
                    "withHealth": 2,
                    "team": "Friendly",
                },
            },
            "level2Ability": {
                "description": "Faint: Summon two 4/4 Rams",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-ram",
                    "withAttack": 4,
                    "withHealth": 4,
                    "team": "Friendly",
                },
            },
            "level3Ability": {
                "description": "Faint: Summon two 6/6 Rams",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-ram",
                    "withAttack": 6,
                    "withHealth": 6,
                    "team": "Friendly",
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091,
                    },
                },
            ],
        },
        "pet-tropical-fish": {
            "name": "Tropical Fish",
            "id": "pet-tropical-fish",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🐠",
            },
            "tier": 3,
            "baseAttack": 2,
            "baseHealth": 4,
            "packs": ["ExpansionPack1"],
            "level1Ability": {
                "description": "End turn: Give adjacent friends +1 Health",
                "trigger": "EndOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "AdjacentFriends"},
                    "healthAmount": 1,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "End turn: Give adjacent friends +2 Health",
                "trigger": "EndOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "AdjacentFriends"},
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "End turn: Give adjacent friends +3 Health",
                "trigger": "EndOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "AdjacentFriends"},
                    "healthAmount": 3,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {"ExpansionPack1": 0.12681358024691358},
                    "perSlot": {"ExpansionPack1": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {"ExpansionPack1": 0.12681358024691358},
                    "perSlot": {"ExpansionPack1": 0.03333333333333333},
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"ExpansionPack1": 0.08328505725105906},
                    "perSlot": {"ExpansionPack1": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {"ExpansionPack1": 0.09090909090909091},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {"ExpansionPack1": 0.09090909090909091},
                },
            ],
        },
        # Tier 4
        "pet-bison": {
            "name": "Bison",
            "id": "pet-bison",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦬",
            },
            "tier": 4,
            "baseAttack": 4,
            "baseHealth": 4,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "End turn: Gain +1/+2 if there is at least one Lvl. 3 friend.",
                "trigger": "EndOfTurnWithLvl3Friend",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 1,
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "End turn: Gain +2/+4 if there is at least one Lvl. 3 friend.",
                "trigger": "EndOfTurnWithLvl3Friend",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 2,
                    "healthAmount": 4,
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "End turn: Gain +3/+6 if there is at least one Lvl. 3 friend.",
                "trigger": "EndOfTurnWithLvl3Friend",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 3,
                    "healthAmount": 6,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-5",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-6",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091,
                    },
                },
            ],
        },
        "pet-blowfish": {
            "name": "Blowfish",
            "id": "pet-blowfish",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐡",
            },
            "tier": 4,
            "baseAttack": 3,
            "baseHealth": 6,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Hurt: Deal 3 damage to a random enemy.",
                "trigger": "Hurt",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "RandomEnemy", "n": 1},
                    "amount": 3,
                },
            },
            "level2Ability": {
                "description": "Hurt: Deal 6 damage to a random enemy.",
                "trigger": "Hurt",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "RandomEnemy", "n": 1},
                    "amount": 6,
                },
            },
            "level3Ability": {
                "description": "Hurt: Deal 9 damage to a random enemy.",
                "trigger": "Hurt",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "RandomEnemy", "n": 1},
                    "amount": 9,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091,
                    },
                },
            ],
        },
        "pet-buffalo": {
            "name": "Buffalo",
            "id": "pet-buffalo",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐃",
            },
            "tier": 4,
            "baseAttack": 5,
            "baseHealth": 5,
            "packs": ["ExpansionPack1"],
            "level1Ability": {
                "description": "Friend bought: Gain +1/+1",
                "trigger": "Buy",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "Friend bought: Gain +2/+2",
                "trigger": "Buy",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "Friend bought: Gain +3/+3",
                "trigger": "Buy",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 3,
                    "healthAmount": 3,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"ExpansionPack1": 0.08328505725105906},
                    "perSlot": {"ExpansionPack1": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-5",
                    "perSlot": {"ExpansionPack1": 0.09090909090909091},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-6",
                    "perSlot": {"ExpansionPack1": 0.09090909090909091},
                },
            ],
        },
        "pet-deer": {  # Note pet-bus spawns with splash-attack by definition
            "name": "Deer",
            "id": "pet-deer",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦌",
            },
            "tier": 4,
            "baseAttack": 2,
            "baseHealth": 2,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Faint: Summon a 5/3 Bus with Chili (splash-attack)",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-bus",
                    "withAttack": 5,
                    "withHealth": 3,
                    "team": "Friendly",
                },
            },
            "level2Ability": {
                "description": "Faint: Summon a 10/6 Bus with Chili (splash-attack)",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-bus",
                    "withAttack": 10,
                    "withHealth": 6,
                    "team": "Friendly",
                },
            },
            "level3Ability": {
                "description": "Faint: Summon a 15/9 Bus with Chili",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-bus",
                    "withAttack": 15,
                    "withHealth": 9,
                    "team": "Friendly",
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-5",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-6",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091,
                    },
                },
            ],
        },
        "pet-hippo": {
            "name": "Hippo",
            "id": "pet-hippo",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦛",
            },
            "tier": 4,
            "baseAttack": 4,
            "baseHealth": 6,
            "packs": ["StandardPack"],
            "level1Ability": {
                "description": "Knock out: Gain +3/+3. Works 3 times.",
                "trigger": "KnockOut",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 3,
                    "healthAmount": 3,
                    "untilEndOfBattle": False,
                },
                "maxTriggers": 3,
            },
            "level2Ability": {
                "description": "Knock out: Gain +6/+6. Works 3 times.",
                "trigger": "KnockOut",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 6,
                    "healthAmount": 6,
                    "untilEndOfBattle": False,
                },
                "maxTriggers": 3,
            },
            "level3Ability": {
                "description": "Knock out: Gain +9/+9. Works 3 times.",
                "trigger": "KnockOut",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 9,
                    "healthAmount": 9,
                    "untilEndOfBattle": False,
                },
                "maxTriggers": 3,
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"StandardPack": 0.08328505725105906},
                    "perSlot": {"StandardPack": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-5",
                    "perSlot": {"StandardPack": 0.09090909090909091},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-6",
                    "perSlot": {"StandardPack": 0.09090909090909091},
                },
            ],
        },
        "pet-llama": {
            "name": "Llama",
            "id": "pet-llama",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦙",
            },
            "tier": 4,
            "baseAttack": 3,
            "baseHealth": 6,
            "packs": ["ExpansionPack1"],
            "level1Ability": {
                "description": "End turn: If you have 4 or less animals, gain +2/+2.",
                "trigger": "EndOfTurnWith4OrLessAnimals",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "End turn: If you have 4 or less animals, gain +4/+4.",
                "trigger": "EndOfTurnWith4OrLessAnimals",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 4,
                    "healthAmount": 4,
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "End turn: If you have 4 or less animals, gain +6/+6.",
                "trigger": "EndOfTurnWith4OrLessAnimals",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 6,
                    "healthAmount": 6,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"ExpansionPack1": 0.08328505725105906},
                    "perSlot": {"ExpansionPack1": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-5",
                    "perSlot": {"ExpansionPack1": 0.09090909090909091},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-6",
                    "perSlot": {"ExpansionPack1": 0.09090909090909091},
                },
            ],
        },
        "pet-lobster": {
            "name": "Lobster",
            "id": "pet-lobster",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🦞",
            },
            "tier": 4,
            "baseAttack": 4,
            "baseHealth": 5,
            "packs": ["ExpansionPack1"],
            "level1Ability": {
                "description": "Friend summoned: Give it +2/+2 when not in battle.",
                "trigger": "Summoned",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "TriggeringEntity"},
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "Friend summoned: Give it +4/+4 when not in battle.",
                "trigger": "Summoned",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "TriggeringEntity"},
                    "attackAmount": 4,
                    "healthAmount": 4,
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "Friend summoned: Give it +6/+6 when not in battle.",
                "trigger": "Summoned",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "TriggeringEntity"},
                    "attackAmount": 6,
                    "healthAmount": 6,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"ExpansionPack1": 0.08328505725105906},
                    "perSlot": {"ExpansionPack1": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-5",
                    "perSlot": {"ExpansionPack1": 0.09090909090909091},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-6",
                    "perSlot": {"ExpansionPack1": 0.09090909090909091},
                },
            ],
        },
        "pet-parrot": {
            "name": "Parrot",
            "id": "pet-parrot",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦜",
            },
            "tier": 4,
            "baseAttack": 4,
            "baseHealth": 2,
            "packs": ["StandardPack"],
            "level1Ability": {
                "description": "End Turn: Copy ability from pet ahead as lvl. 1 until end of battle.",
                "trigger": "EndOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "TransferAbility",
                    "from": {"kind": "FriendAhead", "n": 1},
                    "target": {"kind": "Self"},
                    "level": 1,
                },
            },
            "level2Ability": {
                "description": "End Turn: Copy ability from pet ahead as lvl. 2 until end of battle.",
                "trigger": "EndOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "TransferAbility",
                    "from": {"kind": "FriendAhead", "n": 1},
                    "target": {"kind": "Self"},
                    "level": 2,
                },
            },
            "level3Ability": {
                "description": "End Turn: Copy ability from pet ahead as lvl. 3 until end of battle.",
                "trigger": "EndOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "TransferAbility",
                    "from": {"kind": "FriendAhead", "n": 1},
                    "target": {"kind": "Self"},
                    "level": 3,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"StandardPack": 0.08328505725105906},
                    "perSlot": {"StandardPack": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-5",
                    "perSlot": {"StandardPack": 0.09090909090909091},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-6",
                    "perSlot": {"StandardPack": 0.09090909090909091},
                },
            ],
        },
        "pet-penguin": {  # TODO - check properly choosing 2 lvl2 or higher
            "name": "Penguin",
            "id": "pet-penguin",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐧",
            },
            "tier": 4,
            "baseAttack": 2,
            "baseHealth": 3,
            "packs": ["StandardPack"],
            "level1Ability": {
                "description": "Start turn: Give two Lvl. 2 or 3 friends +1/+1",
                "trigger": "StartOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Level2And3Friends", "n": 2},
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "Start turn: Give two Lvl. 2 or 3 friends +2/+2",
                "trigger": "StartOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Level2And3Friends", "n": 2},
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "Start turn: Give two Lvl. 2 or 3 friends +3/+3",
                "trigger": "StartOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Level2And3Friends", "n": 2},
                    "attackAmount": 3,
                    "healthAmount": 3,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"StandardPack": 0.08328505725105906},
                    "perSlot": {"StandardPack": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-5",
                    "perSlot": {"StandardPack": 0.09090909090909091},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-6",
                    "perSlot": {"StandardPack": 0.09090909090909091},
                },
            ],
        },
        "pet-poodle": {
            "name": "Poodle",
            "id": "pet-poodle",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐩",
            },
            "tier": 5,
            "baseAttack": 2,
            "baseHealth": 2,
            "packs": ["ExpansionPack1"],
            "level1Ability": {
                "description": "End turn: Give +1/+1 to different tier animals.",
                "trigger": "EndOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "DifferentTierAnimals"},
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "End turn: Give +2/+2 to different tier animals.",
                "trigger": "EndOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "DifferentTierAnimals"},
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "End turn: Give +3/+3 to different tier animals.",
                "trigger": "EndOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "DifferentTierAnimals"},
                    "attackAmount": 3,
                    "healthAmount": 3,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"ExpansionPack1": 0.08328505725105906},
                    "perSlot": {"ExpansionPack1": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-7",
                    "perSlot": {"ExpansionPack1": 0.125},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-8",
                    "perSlot": {"ExpansionPack1": 0.125},
                },
            ],
        },
        "pet-skunk": {
            "name": "Skunk",
            "id": "pet-skunk",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦨",
            },
            "tier": 4,
            "baseAttack": 3,
            "baseHealth": 5,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Start of battle: Reduce the highest Health enemy by 33%.",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ReduceHealth",
                    "target": {"kind": "HighestHealthEnemy"},
                    "percentage": 33,
                },
            },
            "level2Ability": {
                "description": "Start of battle: Reduce the highest Health enemy by 66%.",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ReduceHealth",
                    "target": {"kind": "HighestHealthEnemy"},
                    "percentage": 66,
                },
            },
            "level3Ability": {
                "description": "Start of battle: Reduce the highest Health enemy by 99%.",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ReduceHealth",
                    "target": {"kind": "HighestHealthEnemy"},
                    "percentage": 99,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-5",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-6",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091,
                    },
                },
            ],
        },
        "pet-squirrel": {
            "name": "Squirrel",
            "id": "pet-squirrel",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐿",
            },
            "tier": 4,
            "baseAttack": 3,
            "baseHealth": 5,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Start of turn: Discount shop food by 1 gold",
                "trigger": "StartOfTurn",
                "triggeredBy": {"kind": "Self"},
                "effect": {"kind": "DiscountFood", "amount": 1},
            },
            "level2Ability": {
                "description": "Start of turn: Discount shop food by 2 gold",
                "trigger": "StartOfTurn",
                "triggeredBy": {"kind": "Self"},
                "effect": {"kind": "DiscountFood", "amount": 2},
            },
            "level3Ability": {
                "description": "Start of turn: Discount shop food by 3 gold",
                "trigger": "StartOfTurn",
                "triggeredBy": {"kind": "Self"},
                "effect": {"kind": "DiscountFood", "amount": 3},
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-5",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-6",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091,
                    },
                },
            ],
        },
        "pet-turtle": {
            "name": "Turtle",
            "id": "pet-turtle",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐢",
            },
            "tier": 4,
            "baseAttack": 2,
            "baseHealth": 5,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Faint: Give friend behind Melon Armor",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ApplyStatus",
                    "status": "status-melon-armor",
                    "target": {"kind": "FriendBehind", "n": 1},
                },
            },
            "level2Ability": {
                "description": "Faint: Give 2 friends behind Melon Armor",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ApplyStatus",
                    "status": "status-melon-armor",
                    "target": {"kind": "FriendBehind", "n": 2},
                },
            },
            "level3Ability": {
                "description": "Faint: Give 3 friends behind Melon Armor",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ApplyStatus",
                    "status": "status-melon-armor",
                    "target": {"kind": "FriendBehind", "n": 3},
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358,
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091,
                    },
                },
            ],
        },
        "pet-whale": {
            "name": "Whale",
            "id": "pet-whale",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐋",
            },
            "tier": 4,
            "baseAttack": 3,
            "baseHealth": 7,
            "packs": ["StandardPack"],
            "level1Ability": {
                "description": "Start of battle: Swallow friend ahead and release it as a level 1 after fainting.",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "Swallow",
                    "target": {"kind": "FriendAhead", "n": 1},
                },
            },
            "level2Ability": {
                "description": "Start of battle: Swallow friend ahead and release it as a level 2 after fainting.",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "Swallow",
                    "target": {"kind": "FriendAhead", "n": 1},
                },
            },
            "level3Ability": {
                "description": "Start of battle: Swallow friend ahead and release it as a level 3 after fainting.",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "Swallow",
                    "target": {"kind": "FriendAhead", "n": 1},
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"StandardPack": 0.09404935520024527},
                    "perSlot": {"StandardPack": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"StandardPack": 0.08328505725105906},
                    "perSlot": {"StandardPack": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-5",
                    "perSlot": {"StandardPack": 0.09090909090909091},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-6",
                    "perSlot": {"StandardPack": 0.09090909090909091},
                },
            ],
        },
        # Tier 5
        "pet-armadillo": {  # TODO - implement effect
            "name": "Armadillo",
            "id": "pet-armadillo",
            "image": {
                "source": "",
                "commit": "",
                "unicodeCodePoint": "",
            },
            "tier": 5,
            "baseAttack": 2,
            "baseHealth": 10,
            "packs": ["StandardPack"],
            "level1Ability": {
                "description": "Start Battle: Give ALL pets +8 Health",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Self"},
                "effect": {},
            },
            "level2Ability": {
                "description": "Start Battle: Give ALL pets +16 Health",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Self"},
                "effect": {},
            },
            "level3Ability": {
                "description": "Start Battle: Give ALL pets +24 Health",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Self"},
                "effect": {},
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-7",
                    "perSlot": {"StandardPack": 0.125, "ExpansionPack1": 0.125},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-8",
                    "perSlot": {"StandardPack": 0.125, "ExpansionPack1": 0.125},
                },
            ],
        },
        "pet-chicken": {
            "name": "Chicken",
            "id": "pet-chicken",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🐓",
            },
            "tier": 5,
            "baseAttack": 1,
            "baseHealth": 2,
            "packs": ["ExpansionPack1"],
            "level1Ability": {
                "description": "Buy tier 1 animal: Give current and future shop animals +1/+1",
                "trigger": "BuyTier1Animal",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "EachShopAnimal", "includingFuture": True},
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "Buy tier 1 animal: Give current and future shop animals +2/+2",
                "trigger": "BuyTier1Animal",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "EachShopAnimal", "includingFuture": True},
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "Buy tier 1 animal: Give current and future shop animals +3/+3",
                "trigger": "BuyTier1Animal",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "EachShopAnimal", "includingFuture": True},
                    "attackAmount": 3,
                    "healthAmount": 3,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"ExpansionPack1": 0.08328505725105906},
                    "perSlot": {"ExpansionPack1": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-7",
                    "perSlot": {"ExpansionPack1": 0.125},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-8",
                    "perSlot": {"ExpansionPack1": 0.125},
                },
            ],
        },
        "pet-cow": {
            "name": "Cow",
            "id": "pet-cow",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐄",
            },
            "tier": 5,
            "baseAttack": 4,
            "baseHealth": 6,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Buy: Replace food shop with 2 free milk that gives +1/+2.",
                "trigger": "Buy",
                "triggeredBy": {"kind": "Self"},
                "effect": {"kind": "RefillShops", "shop": "Food", "food": "food-milk"},
            },
            "level2Ability": {
                "description": "Buy: Replace food shop with 2 free milk that gives +2/+4.",
                "trigger": "Buy",
                "triggeredBy": {"kind": "Self"},
                "effect": {"kind": "RefillShops", "shop": "Food", "food": "food-milk"},
            },
            "level3Ability": {
                "description": "Buy: Replace food shop with 2 free milk that gives +3/+6.",
                "trigger": "Buy",
                "triggeredBy": {"kind": "Self"},
                "effect": {"kind": "RefillShops", "shop": "Food", "food": "food-milk"},
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-7",
                    "perSlot": {"StandardPack": 0.125, "ExpansionPack1": 0.125},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-8",
                    "perSlot": {"StandardPack": 0.125, "ExpansionPack1": 0.125},
                },
            ],
        },
        "pet-crocodile": {  # TODO - implement "triggers n times"
            "name": "Crocodile",
            "id": "pet-crocodile",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🐊",
            },
            "tier": 5,
            "baseAttack": 8,
            "baseHealth": 4,
            "packs": ["StandardPack"],
            "level1Ability": {
                "description": "Start of battle: Deal 8 damage to the last enemy",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "LastEnemy"},
                    "amount": 8,
                },
            },
            "level2Ability": {
                "description": "Start of battle: Deal 8 damage to the last enemy. Triggers twice.",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "LastEnemy"},
                    "amount": 8,
                },
            },
            "level3Ability": {
                "description": "Start of battle: Deal 8 damage to the last enemy. Triggers thrice.",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "LastEnemy"},
                    "amount": 8,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"StandardPack": 0.08328505725105906},
                    "perSlot": {"StandardPack": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-7",
                    "perSlot": {"StandardPack": 0.125},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-8",
                    "perSlot": {"StandardPack": 0.125},
                },
            ],
        },
        "pet-eagle": {
            "name": "Eagle",
            "id": "pet-eagle",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦅",
            },
            "tier": 5,
            "baseAttack": 6,
            "baseHealth": 5,
            "packs": ["ExpansionPack1"],
            "level1Ability": {
                "description": "Faint: Summon one Lvl. 1 tier 6 animal.",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "SummonRandomPet",
                    "tier": 6,
                    "level": 1,
                    "statsModifier": 1,
                },
            },
            "level2Ability": {
                "description": "Faint: Summon one Lvl. 2 tier 6 animal.",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "SummonRandomPet",
                    "tier": 6,
                    "level": 2,
                    "statsModifier": 2,
                },
            },
            "level3Ability": {
                "description": "Faint: Summon one Lvl. 3 tier 6 animal.",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "SummonRandomPet",
                    "tier": 6,
                    "level": 3,
                    "statsModifier": 3,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"ExpansionPack1": 0.08328505725105906},
                    "perSlot": {"ExpansionPack1": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-7",
                    "perSlot": {"ExpansionPack1": 0.125},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-8",
                    "perSlot": {"ExpansionPack1": 0.125},
                },
            ],
        },
        "pet-goat": {
            "name": "Goat",
            "id": "pet-goat",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐐",
            },
            "tier": 5,
            "baseAttack": 4,
            "baseHealth": 6,
            "packs": ["ExpansionPack1"],
            "level1Ability": {
                "description": "Friend bought: Gain 1 gold.",
                "trigger": "Buy",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {"kind": "GainGold", "amount": 1},
                "maxTriggers": 2,
            },
            "level2Ability": {
                "description": "Friend bought: Gain 2 gold.",
                "trigger": "Buy",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {"kind": "GainGold", "amount": 2},
                "maxTriggers": 2,
            },
            "level3Ability": {
                "description": "Friend bought: Gain 3 gold.",
                "trigger": "Buy",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {"kind": "GainGold", "amount": 3},
                "maxTriggers": 2,
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"ExpansionPack1": 0.08328505725105906},
                    "perSlot": {"ExpansionPack1": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-7",
                    "perSlot": {"ExpansionPack1": 0.125},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-8",
                    "perSlot": {"ExpansionPack1": 0.125},
                },
            ],
        },
        "pet-microbe": {
            "name": "Microbe",
            "id": "pet-microbe",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦠",
            },
            "tier": 4,
            "baseAttack": 1,
            "baseHealth": 1,
            "packs": ["ExpansionPack1"],
            "level1Ability": {
                "description": "Faint: Make all animals Weak.",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ApplyStatus",
                    "status": "status-weak",
                    "target": {"kind": "All"},
                },
            },
            "level2Ability": {
                "description": "Faint: Make all animals Weak.",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ApplyStatus",
                    "status": "status-weak",
                    "target": {"kind": "All"},
                },
            },
            "level3Ability": {
                "description": "Faint: Make all animals Weak.",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ApplyStatus",
                    "status": "status-weak",
                    "target": {"kind": "All"},
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {"ExpansionPack1": 0.09404935520024527},
                    "perSlot": {"ExpansionPack1": 0.024390243902439025},
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"ExpansionPack1": 0.09796001985292535},
                    "perSlot": {"ExpansionPack1": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"ExpansionPack1": 0.08328505725105906},
                    "perSlot": {"ExpansionPack1": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-5",
                    "perSlot": {"ExpansionPack1": 0.09090909090909091},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-6",
                    "perSlot": {"ExpansionPack1": 0.09090909090909091},
                },
            ],
        },
        "pet-monkey": {
            "name": "Monkey",
            "id": "pet-monkey",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐒",
            },
            "tier": 5,
            "baseAttack": 1,
            "baseHealth": 2,
            "packs": ["StandardPack"],
            "level1Ability": {
                "description": "End turn: Give right-most friend +2/+2",
                "trigger": "EndOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "RightMostFriend"},
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "End turn: Give right-most friend +4/+4",
                "trigger": "EndOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "RightMostFriend"},
                    "attackAmount": 4,
                    "healthAmount": 4,
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "End turn: Give right-most friend +6/+6",
                "trigger": "EndOfTurn",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "RightMostFriend"},
                    "attackAmount": 6,
                    "healthAmount": 6,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"StandardPack": 0.08328505725105906},
                    "perSlot": {"StandardPack": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-7",
                    "perSlot": {"StandardPack": 0.125},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-8",
                    "perSlot": {"StandardPack": 0.125},
                },
            ],
        },
        "pet-rhino": {  # TODO - implement "double against tier 1"
            "name": "Rhino",
            "id": "pet-rhino",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦏",
            },
            "tier": 5,
            "baseAttack": 6,
            "baseHealth": 7,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Knock out: Deal 4 damage to the first enemy. Double against tier 1.",
                "trigger": "KnockOut",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "FirstEnemy"},
                    "amount": 4,
                },
            },
            "level2Ability": {
                "description": "Knock out: Deal 8 damage to the first enemy. Double against tier 1.",
                "trigger": "KnockOut",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "FirstEnemy"},
                    "amount": 8,
                },
            },
            "level3Ability": {
                "description": "Knock out: Deal 12 damage to the first enemy. Double against tier 1.",
                "trigger": "KnockOut",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "FirstEnemy"},
                    "amount": 12,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-7",
                    "perSlot": {"StandardPack": 0.125, "ExpansionPack1": 0.125},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-8",
                    "perSlot": {"StandardPack": 0.125, "ExpansionPack1": 0.125},
                },
            ],
        },
        "pet-rooster": {
            "name": "Rooster",
            "id": "pet-rooster",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐓",
            },
            "tier": 5,
            "baseAttack": 6,
            "baseHealth": 5,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Faint: Summon a Chick with 1 health and half the Attack of this.",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {"kind": "SummonPet", "pet": "pet-chick", "team": "Friendly"},
            },
            "level2Ability": {
                "description": "Faint: Summon 2 Chicks with 1 health and half the Attack of this.",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {"kind": "SummonPet", "pet": "pet-chick", "team": "Friendly"},
            },
            "level3Ability": {
                "description": "Faint: Summon 3 Chicks with 1 health and half the Attack of this.",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {"kind": "SummonPet", "pet": "pet-chick", "team": "Friendly"},
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527,
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-5",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-6",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091,
                    },
                },
            ],
        },
        "pet-scorpion": {  # TODO check poison-attack status one shots
            "name": "Scorpion",
            "id": "pet-scorpion",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦂",
            },
            "tier": 5,
            "baseAttack": 1,
            "baseHealth": 1,
            "packs": ["StandardPack", "ExpansionPack1"],
            "status": "status-poison-attack",
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-7",
                    "perSlot": {"StandardPack": 0.125, "ExpansionPack1": 0.125},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-8",
                    "perSlot": {"StandardPack": 0.125, "ExpansionPack1": 0.125},
                },
            ],
        },
        "pet-seal": {
            "name": "Seal",
            "id": "pet-seal",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦭",
            },
            "tier": 5,
            "baseAttack": 3,
            "baseHealth": 8,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Eats shop food: Give 3 random friends +1 attack.",
                "trigger": "EatsShopFood",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "RandomFriend", "n": 3},
                    "attackAmount": 1,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "Eats shop food: Give 3 random friends +2 attack.",
                "trigger": "EatsShopFood",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "RandomFriend", "n": 3},
                    "attackAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "Eats shop food: Give 3 random friends +3 attack.",
                "trigger": "EatsShopFood",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "RandomFriend", "n": 3},
                    "attackAmount": 3,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535,
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-7",
                    "perSlot": {"StandardPack": 0.125, "ExpansionPack1": 0.125},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-8",
                    "perSlot": {"StandardPack": 0.125, "ExpansionPack1": 0.125},
                },
            ],
        },
        "pet-shark": {
            "name": "Shark",
            "id": "pet-shark",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦈",
            },
            "tier": 5,
            "baseAttack": 2,
            "baseHealth": 2,
            "packs": ["StandardPack"],
            "level1Ability": {
                "description": "Friend faints: Gain +2/+2.",
                "trigger": "Faint",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "Friend faints: Gain +4/+4.",
                "trigger": "Faint",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 4,
                    "healthAmount": 4,
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "Friend faints: Gain +6/+6.",
                "trigger": "Faint",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 6,
                    "healthAmount": 6,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"StandardPack": 0.08328505725105906},
                    "perSlot": {"StandardPack": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-7",
                    "perSlot": {"StandardPack": 0.125},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-8",
                    "perSlot": {"StandardPack": 0.125},
                },
            ],
        },
        "pet-turkey": {
            "name": "Turkey",
            "id": "pet-turkey",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦃",
            },
            "tier": 5,
            "baseAttack": 3,
            "baseHealth": 4,
            "packs": ["StandardPack"],
            "level1Ability": {
                "description": "Friend summoned: Give it +3/+1.",
                "trigger": "Summoned",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "TriggeringEntity"},
                    "attackAmount": 3,
                    "healthAmount": 1,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "Friend summoned: Give it +6/+2.",
                "trigger": "Summoned",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "TriggeringEntity"},
                    "attackAmount": 6,
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "Friend summoned: Give it +9/+3.",
                "trigger": "Summoned",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "TriggeringEntity"},
                    "attackAmount": 9,
                    "healthAmount": 3,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {"StandardPack": 0.09796001985292535},
                    "perSlot": {"StandardPack": 0.02040816326530612},
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"StandardPack": 0.08328505725105906},
                    "perSlot": {"StandardPack": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-7",
                    "perSlot": {"StandardPack": 0.125},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-8",
                    "perSlot": {"StandardPack": 0.125},
                },
            ],
        },
        # Tier 6
        "pet-cat": {
            "name": "Cat",
            "id": "pet-cat",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐈‍⬛",
            },
            "tier": 6,
            "baseAttack": 4,
            "baseHealth": 5,
            "packs": ["StandardPack"],
            "level1Ability": {
                "description": "Food with Health and Attack effects are doubled. Works 2 times.",
                "trigger": "PurchaseFood",
                "triggeredBy": {"kind": "Self"},
                "effect": {"kind": "FoodMultiplier", "amount": 2},
                "maxTriggers": 2,
            },
            "level2Ability": {
                "description": "Food with Health and Attack effects are tripled. Works 2 times.",
                "trigger": "PurchaseFood",
                "triggeredBy": {"kind": "Self"},
                "effect": {"kind": "FoodMultiplier", "amount": 3},
                "maxTriggers": 2,
            },
            "level3Ability": {
                "description": "Food with Health and Attack effects are quadrupled. Works 2 times.",
                "trigger": "PurchaseFood",
                "triggeredBy": {"kind": "Self"},
                "effect": {"kind": "FoodMultiplier", "amount": 4},
                "maxTriggers": 2,
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"StandardPack": 0.08328505725105906},
                    "perSlot": {"StandardPack": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-9",
                    "perSlot": {"StandardPack": 0.1111111111111111},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-10",
                    "perSlot": {"StandardPack": 0.1111111111111111},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-11",
                    "perSlot": {"StandardPack": 0.1111111111111111},
                },
            ],
        },
        "pet-boar": {
            "name": "Boar",
            "id": "pet-boar",
            "image": {
                "source": "noto-emoji",
                "commit": "f2a4f72bffe0212c72949a22698be235269bfab5",
                "unicodeCodePoint": "🐗",
            },
            "tier": 6,
            "baseAttack": 10,
            "baseHealth": 6,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Before attack: Gain +4/+2.",
                "trigger": "BeforeAttack",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 4,
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "Before attack: Gain +8/+4.",
                "trigger": "BeforeAttack",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 8,
                    "healthAmount": 4,
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "Before attack: Gain +12/+6.",
                "trigger": "BeforeAttack",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 12,
                    "healthAmount": 6,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-9",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-10",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-11",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
            ],
        },
        "pet-dragon": {
            "name": "Dragon",
            "id": "pet-dragon",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐉",
            },
            "tier": 6,
            "baseAttack": 6,
            "baseHealth": 8,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Buy tier 1 animal: Give all friends +1/+1. Works 5 times.",
                "trigger": "BuyTier1Animal",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "EachFriend"},
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "untilEndOfBattle": False,
                },
                "maxTriggers": 5,
            },
            "level2Ability": {
                "description": "Buy tier 1 animal: Give all friends +2/+2. Works 5 times.",
                "trigger": "BuyTier1Animal",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "EachFriend"},
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
                "maxTriggers": 5,
            },
            "level3Ability": {
                "description": "Buy tier 1 animal: Give all friends +3/+3. Works 5 times.",
                "trigger": "BuyTier1Animal",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "EachFriend"},
                    "attackAmount": 3,
                    "healthAmount": 3,
                    "untilEndOfBattle": False,
                },
                "maxTriggers": 5,
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-9",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-10",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-11",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
            ],
        },
        "pet-fly": {
            "name": "Fly",
            "id": "pet-fly",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🪰",
            },
            "tier": 6,
            "baseAttack": 4,
            "baseHealth": 4,
            "packs": ["StandardPack"],
            "level1Ability": {
                "description": "Friend faints: Summon a 4/4 fly in its place (Max 3 times)",
                "trigger": "Faint",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-zombie-fly",
                    "withAttack": 4,
                    "withHealth": 4,
                    "team": "Friendly",
                },
                "maxTriggers": 3,
            },
            "level2Ability": {
                "description": "Friend faints: Summon a 8/8 fly in its place (Max 3 times)",
                "trigger": "Faint",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-zombie-fly",
                    "withAttack": 8,
                    "withHealth": 8,
                    "team": "Friendly",
                },
                "maxTriggers": 3,
            },
            "level3Ability": {
                "description": "Friend faints: Summon a 12/12 fly in its place (Max 3 times)",
                "trigger": "Faint",
                "triggeredBy": {"kind": "EachFriend"},
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-zombie-fly",
                    "withAttack": 12,
                    "withHealth": 12,
                    "team": "Friendly",
                },
                "maxTriggers": 3,
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"StandardPack": 0.08328505725105906},
                    "perSlot": {"StandardPack": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-9",
                    "perSlot": {"StandardPack": 0.1111111111111111},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-10",
                    "perSlot": {"StandardPack": 0.1111111111111111},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-11",
                    "perSlot": {"StandardPack": 0.1111111111111111},
                },
            ],
        },
        "pet-gorilla": {
            "name": "Gorilla",
            "id": "pet-gorilla",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦍",
            },
            "tier": 6,
            "baseAttack": 7,
            "baseHealth": 10,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Hurt: Gain Coconut Shield. Works 1 time per turn.",
                "trigger": "Hurt",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ApplyStatus",
                    "status": "status-coconut-shield",
                    "target": {"kind": "Self"},
                },
                "maxTriggers": 1,
            },
            "level2Ability": {
                "description": "Hurt: Gain Coconut Shield. Works 2 times per turn.",
                "trigger": "Hurt",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ApplyStatus",
                    "status": "status-coconut-shield",
                    "target": {"kind": "Self"},
                },
                "maxTriggers": 2,
            },
            "level3Ability": {
                "description": "Hurt: Gain Coconut Shield. Works 3 times per turn.",
                "trigger": "Hurt",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ApplyStatus",
                    "status": "status-coconut-shield",
                    "target": {"kind": "Self"},
                },
                "maxTriggers": 3,
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-9",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-10",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-11",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
            ],
        },
        "pet-leopard": {
            "name": "Leopard",
            "id": "pet-leopard",
            "image": {
                "source": "fxemoji",
                "commit": "270af343bee346d8221f87806d2b1eee0438431a",
                "name": "leopardside",
                "unicodeCodePoint": "🐆",
            },
            "tier": 6,
            "baseAttack": 10,
            "baseHealth": 4,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Start of battle: Deal 50% Attack damage to a random enemy.",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "RandomEnemy", "n": 1},
                    "amount": {"attackDamagePercent": 50},
                },
            },
            "level2Ability": {
                "description": "Start of battle: Deal 50% Attack damage to 2 random enemies.",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "RandomEnemy", "n": 2},
                    "amount": {"attackDamagePercent": 50},
                },
            },
            "level3Ability": {
                "description": "Start of battle: Deal 50% Attack damage to 3 random enemies.",
                "trigger": "StartOfBattle",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "RandomEnemy", "n": 3},
                    "amount": {"attackDamagePercent": 50},
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-9",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-10",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-11",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
            ],
        },
        "pet-mammoth": {
            "name": "Mammoth",
            "id": "pet-mammoth",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦣",
            },
            "tier": 6,
            "baseAttack": 4,
            "baseHealth": 12,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "Faint: Give all friends +2/+2",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "target": {"kind": "EachFriend"},
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "Faint: Give all friends +4/+4",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 4,
                    "healthAmount": 4,
                    "target": {"kind": "EachFriend"},
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "Faint: Give all friends +6/+6",
                "trigger": "Faint",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 6,
                    "healthAmount": 6,
                    "target": {"kind": "EachFriend"},
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-9",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-10",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-11",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
            ],
        },
        "pet-octopus": {
            "name": "Octopus",
            "id": "pet-octopus",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐙",
            },
            "tier": 6,
            "baseAttack": 8,
            "baseHealth": 8,
            "packs": ["ExpansionPack1"],
            "level1Ability": {
                "description": "Level-up: Gain +8/+8.",
                "trigger": "LevelUp",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "Self"},
                    "attackAmount": 8,
                    "healthAmount": 8,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "Level-up: Gain +8/+8 and a new ability.",
                "trigger": "LevelUp",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "AllOf",
                    "effects": [
                        {
                            "kind": "ModifyStats",
                            "target": {"kind": "Self"},
                            "attackAmount": 8,
                            "healthAmount": 8,
                            "untilEndOfBattle": False,
                        },
                        {"kind": "GainAbility", "target": {"kind": "Self"}},
                    ],
                },
            },
            "level3Ability": {
                "description": "Before attack: Deal 5 damage to all enemies",
                "trigger": "BeforeAttack",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "EachEnemy"},
                    "amount": 5,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"ExpansionPack1": 0.08328505725105906},
                    "perSlot": {"ExpansionPack1": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-9",
                    "perSlot": {"ExpansionPack1": 0.1111111111111111},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-10",
                    "perSlot": {"ExpansionPack1": 0.1111111111111111},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-11",
                    "perSlot": {"ExpansionPack1": 0.1111111111111111},
                },
            ],
        },
        "pet-sauropod": {
            "name": "Sauropod",
            "id": "pet-sauropod",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦕",
            },
            "tier": 6,
            "baseAttack": 4,
            "baseHealth": 12,
            "packs": ["ExpansionPack1"],
            "level1Ability": {
                "description": "Buy food: Gain 1 gold.",
                "trigger": "BuyFood",
                "triggeredBy": {"kind": "Player"},
                "effect": {"kind": "GainGold", "amount": 1},
                "maxTriggers": 3,
            },
            "level2Ability": {
                "description": "Buy food: Gain 2 gold.",
                "trigger": "BuyFood",
                "triggeredBy": {"kind": "Player"},
                "effect": {"kind": "GainGold", "amount": 1},
                "maxTriggers": 3,
            },
            "level3Ability": {
                "description": "Buy food: Gain 3 gold.",
                "trigger": "BuyFood",
                "triggeredBy": {"kind": "Player"},
                "effect": {"kind": "GainGold", "amount": 1},
                "maxTriggers": 3,
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"ExpansionPack1": 0.08328505725105906},
                    "perSlot": {"ExpansionPack1": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-9",
                    "perSlot": {"ExpansionPack1": 0.1111111111111111},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-10",
                    "perSlot": {"ExpansionPack1": 0.1111111111111111},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-11",
                    "perSlot": {"ExpansionPack1": 0.1111111111111111},
                },
            ],
        },
        "pet-snake": {
            "name": "Snake",
            "id": "pet-snake",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐍",
            },
            "tier": 6,
            "baseAttack": 8,
            "baseHealth": 3,
            "packs": ["StandardPack"],
            "level1Ability": {
                "description": "Friend ahead attacks: Deal 5 damage to a random enemy.",
                "trigger": "AfterAttack",
                "triggeredBy": {"kind": "FriendAhead", "n": 1},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "RandomEnemy", "n": 1},
                    "amount": 5,
                },
            },
            "level2Ability": {
                "description": "Friend ahead attacks: Deal 10 damage to a random enemy.",
                "trigger": "AfterAttack",
                "triggeredBy": {"kind": "FriendAhead", "n": 1},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "RandomEnemy", "n": 1},
                    "amount": 10,
                },
            },
            "level3Ability": {
                "description": "Friend ahead attacks: Deal 15 damage to a random enemy.",
                "trigger": "AfterAttack",
                "triggeredBy": {"kind": "FriendAhead", "n": 1},
                "effect": {
                    "kind": "DealDamage",
                    "target": {"kind": "RandomEnemy", "n": 1},
                    "amount": 15,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"StandardPack": 0.08328505725105906},
                    "perSlot": {"StandardPack": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-9",
                    "perSlot": {"StandardPack": 0.1111111111111111},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-10",
                    "perSlot": {"StandardPack": 0.1111111111111111},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-11",
                    "perSlot": {"StandardPack": 0.1111111111111111},
                },
            ],
        },
        "pet-tiger": {
            "name": "Tiger",
            "id": "pet-tiger",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐅",
            },
            "tier": 6,
            "baseAttack": 6,
            "baseHealth": 4,
            "packs": ["StandardPack", "ExpansionPack1"],
            "level1Ability": {
                "description": "The friend ahead repeats their ability in battle as if they were level 1.",
                "trigger": "CastsAbility",
                "triggeredBy": {"kind": "FriendAhead", "n": 1},
                "effect": {
                    "kind": "RepeatAbility",
                    "target": {"kind": "TriggeringEntity"},
                    "level": 1,
                },
            },
            "level2Ability": {
                "description": "The friend ahead repeats their ability in battle as if they were level 2.",
                "trigger": "CastsAbility",
                "triggeredBy": {"kind": "FriendAhead", "n": 1},
                "effect": {
                    "kind": "RepeatAbility",
                    "target": {"kind": "TriggeringEntity"},
                    "level": 2,
                },
            },
            "level3Ability": {
                "description": "The friend ahead repeats their ability in battle as if they were level 3.",
                "trigger": "CastsAbility",
                "triggeredBy": {"kind": "FriendAhead", "n": 1},
                "effect": {
                    "kind": "RepeatAbility",
                    "target": {"kind": "TriggeringEntity"},
                    "level": 3,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906,
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-9",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-10",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "levelup",
                    "turn": "turn-11",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
            ],
        },
        "pet-tyrannosaurus": {
            "name": "Tyrannosaurus",
            "id": "pet-tyrannosaurus",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦖",
            },
            "tier": 6,
            "baseAttack": 9,
            "baseHealth": 4,
            "packs": ["ExpansionPack1"],
            "level1Ability": {
                "description": "End turn: If you have 3 or more gold, give all +2/+1",
                "trigger": "EndOfTurnWith3PlusGold",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "EachFriend"},
                    "attackAmount": 2,
                    "healthAmount": 1,
                    "untilEndOfBattle": False,
                },
            },
            "level2Ability": {
                "description": "End turn: If you have 3 or more gold, give all +4/+2",
                "trigger": "EndOfTurnWith3PlusGold",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "EachFriend"},
                    "attackAmount": 4,
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "level3Ability": {
                "description": "End turn: If you have 3 or more gold, give all +6/+3",
                "trigger": "EndOfTurnWith3PlusGold",
                "triggeredBy": {"kind": "Player"},
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "EachFriend"},
                    "attackAmount": 6,
                    "healthAmount": 3,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"ExpansionPack1": 0.08328505725105906},
                    "perSlot": {"ExpansionPack1": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-9",
                    "perSlot": {"ExpansionPack1": 0.1111111111111111},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-10",
                    "perSlot": {"ExpansionPack1": 0.1111111111111111},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-11",
                    "perSlot": {"ExpansionPack1": 0.1111111111111111},
                },
            ],
        },
        "pet-wolverine": {  # TODO - implement
            "name": "Wolverine",
            "id": "pet-wolverine",
            "image": {
                "source": "",
                "commit": "",
                "unicodeCodePoint": "",
            },
            "tier": 6,
            "baseAttack": 5,
            "baseHealth": 7,
            "packs": ["StandardPack"],
            "level1Ability": {
                "description": "4 friends hurt: remove 3 health from all enemies",
                "trigger": "",
                # "triggeredBy": {"kind": "FriendAhead", "n": 1},
                "effect": {},
            },
            "level2Ability": {
                "description": "4 friends hurt: remove 6 health from all enemies",
                "trigger": "",
                # "triggeredBy": {"kind": "FriendAhead", "n": 1},
                "effect": {},
            },
            "level3Ability": {
                "description": "4 friends hurt: remove 9 health from all enemies",
                "trigger": "",
                # "triggeredBy": {"kind": "FriendAhead", "n": 1},
                "effect": {},
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {"StandardPack": 0.08328505725105906},
                    "perSlot": {"StandardPack": 0.017241379310344827},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-9",
                    "perSlot": {"StandardPack": 0.1111111111111111},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-10",
                    "perSlot": {"StandardPack": 0.1111111111111111},
                },
                {
                    "kind": "levelup",
                    "turn": "turn-11",
                    "perSlot": {"StandardPack": 0.1111111111111111},
                },
            ],
        },
        # Non-Shop pets
        "pet-zombie-cricket": {
            "name": "Zombie Cricket",
            "id": "pet-zombie-cricket",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦗",
            },
            "packs": ["StandardPack", "ExpansionPack1"],
            "tier": "Summoned",
            "baseAttack": "?",
            "baseHealth": "?",
        },
        "pet-bus": {
            "name": "Bus",
            "id": "pet-bus",
            "image": {
                "source": "noto-emoji",
                "commit": "f2a4f72bffe0212c72949a22698be235269bfab5",
                "unicodeCodePoint": "🚌",
            },
            "packs": ["StandardPack", "ExpansionPack1"],
            "tier": "Summoned",
            "baseAttack": "?",
            "baseHealth": "?",
            "status": "status-splash-attack",
        },
        "pet-zombie-fly": {
            "name": "Zombie Fly",
            "id": "pet-zombie-fly",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🪰",
            },
            "packs": ["StandardPack"],
            "tier": "Summoned",
            "baseAttack": "?",
            "baseHealth": "?",
        },
        "pet-dirty-rat": {
            "name": "Dirty Rat",
            "id": "pet-dirty-rat",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐀",
            },
            "packs": ["StandardPack", "ExpansionPack1"],
            "tier": "Summoned",
            "baseAttack": 1,
            "baseHealth": 1,
        },
        "pet-chick": {
            "name": "Chick",
            "id": "pet-chick",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐤",
            },
            "packs": ["StandardPack", "ExpansionPack1"],
            "tier": "Summoned",
            "baseAttack": "?",
            "baseHealth": 1,
        },
        "pet-ram": {
            "name": "Ram",
            "id": "pet-ram",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐏",
            },
            "packs": ["StandardPack", "ExpansionPack1"],
            "tier": "Summoned",
            "baseAttack": "?",
            "baseHealth": "?",
        },
        "pet-butterfly": {
            "name": "Butterfly",
            "id": "pet-butterfly",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦋",
            },
            "notes": "Summoned: Copy stats of the strongest friend (highest attack and health combined).",
            "tier": "Summoned",
            "baseAttack": 1,
            "baseHealth": 1,
            "packs": ["ExpansionPack1"],
            "level1Ability": {
                "description": "Copy stats of the strongest friend (highest attack and health combined).",
                "trigger": "Summoned",
                "triggeredBy": {"kind": "Self"},
                "effect": {
                    "kind": "TransferStats",
                    "copyAttack": True,
                    "copyHealth": True,
                    "from": {"kind": "StrongestFriend"},
                    "target": {"kind": "Self"},
                },
            },
        },
        "pet-bee": {
            "name": "Bee",
            "id": "pet-bee",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🐝",
            },
            "packs": ["StandardPack", "ExpansionPack1"],
            "tier": "Summoned",
            "baseAttack": 1,
            "baseHealth": 1,
        },
    },
    "foods": {
        "food-apple": {
            "name": "Apple",
            "id": "food-apple",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🍎",
            },
            "tier": 1,
            "packs": ["StandardPack", "ExpansionPack1"],
            "ability": {
                "description": "Give an animal +1/+1.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "Buy",
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "PurchaseTarget"},
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {"StandardPack": 0.5, "ExpansionPack1": 0.5},
                    "perSlot": {"StandardPack": 0.5, "ExpansionPack1": 0.5},
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {"StandardPack": 0.5, "ExpansionPack1": 0.5},
                    "perSlot": {"StandardPack": 0.5, "ExpansionPack1": 0.5},
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.3599999999999999,
                        "ExpansionPack1": 0.3599999999999999,
                    },
                    "perSlot": {"StandardPack": 0.2, "ExpansionPack1": 0.2},
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.3599999999999999,
                        "ExpansionPack1": 0.3599999999999999,
                    },
                    "perSlot": {"StandardPack": 0.2, "ExpansionPack1": 0.2},
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966,
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966,
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232,
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232,
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375,
                    },
                    "perSlot": {"StandardPack": 0.0625, "ExpansionPack1": 0.0625},
                },
            ],
        },
        "food-honey": {
            "name": "Honey",
            "id": "food-honey",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🍯",
            },
            "tier": 1,
            "packs": ["StandardPack", "ExpansionPack1"],
            "ability": {
                "description": "Give an animal Honey Bee.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "Buy",
                "effect": {
                    "kind": "ApplyStatus",
                    "target": {"kind": "PurchaseTarget"},
                    "status": "status-honey-bee",
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {"StandardPack": 0.5, "ExpansionPack1": 0.5},
                    "perSlot": {"StandardPack": 0.5, "ExpansionPack1": 0.5},
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {"StandardPack": 0.5, "ExpansionPack1": 0.5},
                    "perSlot": {"StandardPack": 0.5, "ExpansionPack1": 0.5},
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.3599999999999999,
                        "ExpansionPack1": 0.3599999999999999,
                    },
                    "perSlot": {"StandardPack": 0.2, "ExpansionPack1": 0.2},
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.3599999999999999,
                        "ExpansionPack1": 0.3599999999999999,
                    },
                    "perSlot": {"StandardPack": 0.2, "ExpansionPack1": 0.2},
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966,
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966,
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232,
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232,
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375,
                    },
                    "perSlot": {"StandardPack": 0.0625, "ExpansionPack1": 0.0625},
                },
            ],
        },
        "food-cupcake": {
            "name": "Cupcake",
            "id": "food-cupcake",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🧁",
            },
            "tier": 2,
            "packs": ["StandardPack", "ExpansionPack1"],
            "ability": {
                "description": "Give an animal +3/+3 until end of battle.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "Buy",
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "PurchaseTarget"},
                    "attackAmount": 3,
                    "healthAmount": 3,
                    "untilEndOfBattle": True,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.3599999999999999,
                        "ExpansionPack1": 0.3599999999999999,
                    },
                    "perSlot": {"StandardPack": 0.2, "ExpansionPack1": 0.2},
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.3599999999999999,
                        "ExpansionPack1": 0.3599999999999999,
                    },
                    "perSlot": {"StandardPack": 0.2, "ExpansionPack1": 0.2},
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966,
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966,
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232,
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232,
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375,
                    },
                    "perSlot": {"StandardPack": 0.0625, "ExpansionPack1": 0.0625},
                },
            ],
        },
        "food-meat-bone": {
            "name": "Meat Bone",
            "id": "food-meat-bone",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🍖",
            },
            "tier": 2,
            "packs": ["StandardPack", "ExpansionPack1"],
            "ability": {
                "description": "Give an animal Bone Attack.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "Buy",
                "effect": {
                    "kind": "ApplyStatus",
                    "target": {"kind": "PurchaseTarget"},
                    "status": "status-bone-attack",
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.3599999999999999,
                        "ExpansionPack1": 0.3599999999999999,
                    },
                    "perSlot": {"StandardPack": 0.2, "ExpansionPack1": 0.2},
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.3599999999999999,
                        "ExpansionPack1": 0.3599999999999999,
                    },
                    "perSlot": {"StandardPack": 0.2, "ExpansionPack1": 0.2},
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966,
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966,
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232,
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232,
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375,
                    },
                    "perSlot": {"StandardPack": 0.0625, "ExpansionPack1": 0.0625},
                },
            ],
        },
        "food-sleeping-pill": {
            "name": "Sleeping Pill",
            "id": "food-sleeping-pill",
            "image": {
                "source": "fxemoji",
                "commit": "270af343bee346d8221f87806d2b1eee0438431a",
                "unicodeCodePoint": "💊",
                "name": "pill",
            },
            "notes": "This costs 1 gold.",
            "tier": 2,
            "packs": ["StandardPack", "ExpansionPack1"],
            "cost": 1,
            "ability": {
                "description": "Make a friendly animal faint.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "Buy",
                "effect": {"kind": "Faint", "target": {"kind": "PurchaseTarget"}},
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.3599999999999999,
                        "ExpansionPack1": 0.3599999999999999,
                    },
                    "perSlot": {"StandardPack": 0.2, "ExpansionPack1": 0.2},
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.3599999999999999,
                        "ExpansionPack1": 0.3599999999999999,
                    },
                    "perSlot": {"StandardPack": 0.2, "ExpansionPack1": 0.2},
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966,
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966,
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232,
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232,
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375,
                    },
                    "perSlot": {"StandardPack": 0.0625, "ExpansionPack1": 0.0625},
                },
            ],
        },
        "food-garlic": {
            "name": "Garlic",
            "id": "food-garlic",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🧄",
            },
            "tier": 3,
            "packs": ["StandardPack", "ExpansionPack1"],
            "ability": {
                "description": "Give an animal Garlic Armor.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "Buy",
                "effect": {
                    "kind": "ApplyStatus",
                    "target": {"kind": "PurchaseTarget"},
                    "status": "status-garlic-armor",
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966,
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966,
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232,
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232,
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375,
                    },
                    "perSlot": {"StandardPack": 0.0625, "ExpansionPack1": 0.0625},
                },
            ],
        },
        "food-salad-bowl": {
            "name": "Salad Bowl",
            "id": "food-salad-bowl",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🥗",
            },
            "tier": 3,
            "packs": ["StandardPack", "ExpansionPack1"],
            "ability": {
                "description": "Give 2 random animals +1/+1.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "Buy",
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "RandomFriend", "n": 2},
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966,
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966,
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232,
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232,
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375,
                    },
                    "perSlot": {"StandardPack": 0.0625, "ExpansionPack1": 0.0625},
                },
            ],
        },
        "food-canned-food": {
            "name": "Canned Food",
            "id": "food-canned-food",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🥫",
            },
            "tier": 4,
            "packs": ["StandardPack", "ExpansionPack1"],
            "ability": {
                "description": "Give all current and future shop animals +2/+1.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "Buy",
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "EachShopAnimal", "includingFuture": True},
                    "attackAmount": 2,
                    "healthAmount": 1,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232,
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232,
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375,
                    },
                    "perSlot": {"StandardPack": 0.0625, "ExpansionPack1": 0.0625},
                },
            ],
        },
        "food-pear": {
            "name": "Pear",
            "id": "food-pear",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🍐",
            },
            "tier": 4,
            "packs": ["StandardPack", "ExpansionPack1"],
            "ability": {
                "description": "Give an animal +2/+2.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "Buy",
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "PurchaseTarget"},
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766,
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232,
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232,
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375,
                    },
                    "perSlot": {"StandardPack": 0.0625, "ExpansionPack1": 0.0625},
                },
            ],
        },
        "food-chili": {
            "name": "Chili",
            "id": "food-chili",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🌶",
            },
            "tier": 5,
            "packs": ["StandardPack", "ExpansionPack1"],
            "ability": {
                "description": "Give an animal Splash Attack.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "Buy",
                "effect": {
                    "kind": "ApplyStatus",
                    "target": {"kind": "PurchaseTarget"},
                    "status": "status-splash-attack",
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232,
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232,
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375,
                    },
                    "perSlot": {"StandardPack": 0.0625, "ExpansionPack1": 0.0625},
                },
            ],
        },
        "food-chocolate": {
            "name": "Chocolate",
            "id": "food-chocolate",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🍫",
            },
            "tier": 5,
            "packs": ["StandardPack", "ExpansionPack1"],
            "ability": {
                "description": "Give an animal +1 Experience.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "Buy",
                "effect": {
                    "kind": "GainExperience",
                    "target": {"kind": "PurchaseTarget"},
                    "amount": 1,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232,
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232,
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375,
                    },
                    "perSlot": {"StandardPack": 0.0625, "ExpansionPack1": 0.0625},
                },
            ],
        },
        "food-sushi": {
            "name": "Sushi",
            "id": "food-sushi",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🍣",
            },
            "tier": 5,
            "packs": ["StandardPack", "ExpansionPack1"],
            "ability": {
                "description": "Give 3 random animals +1/+1.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "Buy",
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "RandomFriend", "n": 3},
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232,
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232,
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333,
                    },
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375,
                    },
                    "perSlot": {"StandardPack": 0.0625, "ExpansionPack1": 0.0625},
                },
            ],
        },
        "food-melon": {
            "name": "Melon",
            "id": "food-melon",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🍈",
            },
            "tier": 6,
            "packs": ["StandardPack", "ExpansionPack1"],
            "ability": {
                "description": "Give an animal Melon Armor.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "Buy",
                "effect": {
                    "kind": "ApplyStatus",
                    "target": {"kind": "PurchaseTarget"},
                    "status": "status-melon-armor",
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375,
                    },
                    "perSlot": {"StandardPack": 0.0625, "ExpansionPack1": 0.0625},
                }
            ],
        },
        "food-mushroom": {
            "name": "Mushroom",
            "id": "food-mushroom",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🍄",
            },
            "tier": 6,
            "packs": ["StandardPack", "ExpansionPack1"],
            "ability": {
                "description": "Give an animal Extra Life.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "Buy",
                "effect": {
                    "kind": "ApplyStatus",
                    "target": {"kind": "PurchaseTarget"},
                    "status": "status-extra-life",
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375,
                    },
                    "perSlot": {"StandardPack": 0.0625, "ExpansionPack1": 0.0625},
                }
            ],
        },
        "food-pizza": {
            "name": "Pizza",
            "id": "food-pizza",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🍕",
            },
            "tier": 6,
            "packs": ["StandardPack", "ExpansionPack1"],
            "ability": {
                "description": "Give 2 random animals +2/+2.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "Buy",
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "RandomFriend", "n": 2},
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375,
                    },
                    "perSlot": {"StandardPack": 0.0625, "ExpansionPack1": 0.0625},
                }
            ],
        },
        "food-steak": {
            "name": "Steak",
            "id": "food-steak",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🥩",
            },
            "tier": 6,
            "packs": ["StandardPack", "ExpansionPack1"],
            "ability": {
                "description": "Give an animal Steak Attack.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "Buy",
                "effect": {
                    "kind": "ApplyStatus",
                    "target": {"kind": "PurchaseTarget"},
                    "status": "status-steak-attack",
                },
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375,
                    },
                    "perSlot": {"StandardPack": 0.0625, "ExpansionPack1": 0.0625},
                }
            ],
        },
        "food-milk": {
            "name": "Milk",
            "id": "food-milk",
            "notes": "This is free!",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🥛",
            },
            "tier": "Summoned",
            "packs": ["StandardPack", "ExpansionPack1"],
            "cost": 0,
            "ability": {
                "description": "Give an animal +1/2/3 attack and +2/4/6 health (depending on level of Cow).",
                "triggeredBy": {"kind": "Self"},
                "trigger": "Buy",
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "PurchaseTarget"},
                    "attackAmount": 1,
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
        },
        "food-better-apple": {
            "name": "Better Apple",
            "id": "food-better-apple",
            "notes": "Stocked by Worm",
            "image": {
                "source": "",
                "commit": "",
                "unicodeCodePoint": "",
            },
            "tier": "Summoned",
            "packs": ["StandardPack"],
            "cost": 2,
            "ability": {
                "description": "Give an animal +2/+2.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "Buy",
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "PurchaseTarget"},
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False,
                },
            },
        },
        "food-best-apple": {
            "name": "Best Apple",
            "id": "food-best-apple",
            "notes": "Stocked by Worm",
            "image": {
                "source": "",
                "commit": "",
                "unicodeCodePoint": "",
            },
            "tier": "Summoned",
            "packs": ["StandardPack"],
            "cost": 2,
            "ability": {
                "description": "Give an animal +3/+3.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "Buy",
                "effect": {
                    "kind": "ModifyStats",
                    "target": {"kind": "PurchaseTarget"},
                    "attackAmount": 3,
                    "healthAmount": 3,
                    "untilEndOfBattle": False,
                },
            },
        },
    },
    "statuses": {
        "status-weak": {
            "name": "Weak",
            "id": "status-weak",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "🦠",
            },
            "ability": {
                "description": "Take 3 extra damage.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "WhenDamaged",
                "effect": {
                    "kind": "ModifyDamage",
                    "damageModifier": 3,
                    "appliesOnce": False,
                },
            },
        },
        "status-coconut-shield": {
            "name": "Coconut Shield",
            "id": "status-coconut-shield",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🥥",
            },
            "ability": {
                "description": "Ignore damage once.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "WhenDamaged",
                "effect": {
                    "kind": "ModifyDamage",
                    "damageModifier": None,
                    "appliesOnce": True,
                },
            },
        },
        "status-honey-bee": {
            "name": "Honey Bee",
            "id": "status-honey-bee",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🍯",
            },
            "ability": {
                "description": "Summon a 1/1 Bee after fainting.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "Faint",
                "effect": {"kind": "SummonPet", "pet": "pet-bee", "team": "Friendly"},
            },
        },
        "status-bone-attack": {
            "name": "Bone Attack",
            "id": "status-bone-attack",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🍖",
            },
            "ability": {
                "description": "Attack for 5 more damage.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "WhenAttacking",
                "effect": {
                    "kind": "ModifyDamage",
                    "damageModifier": 5,
                    "appliesOnce": False,
                },
            },
        },
        "status-garlic-armor": {
            "name": "Garlic Armor",
            "id": "status-garlic-armor",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🧄",
            },
            "ability": {
                "description": "Take 2 less damage.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "WhenDamaged",
                "effect": {
                    "kind": "ModifyDamage",
                    "damageModifier": -2,
                    "appliesOnce": False,
                },
            },
        },
        "status-splash-attack": {
            "name": "Splash Attack",
            "id": "status-splash-attack",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🌶",
            },
            "ability": {
                "description": "Attack second enemy for 5 damage.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "WhenAttacking",
                "effect": {"kind": "SplashDamage", "amount": 5},
            },
        },
        "status-melon-armor": {
            "name": "Melon Armor",
            "id": "status-melon-armor",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🍈",
            },
            "ability": {
                "description": "Take 20 damage less, once.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "WhenDamaged",
                "effect": {
                    "kind": "ModifyDamage",
                    "damageModifier": -20,
                    "appliesOnce": True,
                },
            },
        },
        "status-extra-life": {
            "name": "Extra Life",
            "id": "status-extra-life",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🍄",
            },
            "ability": {
                "description": "Come back as a 1/1 after fainting",
                "triggeredBy": {"kind": "Self"},
                "trigger": "Faint",
                "effect": {"kind": "RespawnPet", "baseAttack": 1, "baseHealth": 1},
            },
        },
        "status-steak-attack": {
            "name": "Steak Attack",
            "id": "status-steak-attack",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🥩",
            },
            "ability": {
                "description": "Attack for 20 more damage, once.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "WhenAttacking",
                "effect": {
                    "kind": "ModifyDamage",
                    "damageModifier": 20,
                    "appliesOnce": True,
                },
            },
        },
        "status-poison-attack": {
            "name": "Poison Attack",
            "id": "status-poison-attack",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "🥜",
            },
            "ability": {
                "description": "Knock out any animal hit by this.",
                "triggeredBy": {"kind": "Self"},
                "trigger": "WhenAttacking",
                "effect": {
                    "kind": "ModifyDamage",
                    "damageModifier": None,
                    "appliesOnce": False,
                },
            },
        },
    },
    "turns": {
        "turn-1": {
            "name": "Turn 1",
            "id": "turn-1",
            "index": 1,
            "foodShopSlots": 1,
            "animalShopSlots": 3,
            "livesLost": 1,
            "tiersAvailable": 1,
            "levelUpTier": 2,
        },
        "turn-2": {
            "name": "Turn 2",
            "id": "turn-2",
            "index": 2,
            "foodShopSlots": 1,
            "animalShopSlots": 3,
            "livesLost": 1,
            "tiersAvailable": 1,
            "levelUpTier": 2,
        },
        "turn-3": {
            "name": "Turn 3",
            "id": "turn-3",
            "index": 3,
            "foodShopSlots": 2,
            "animalShopSlots": 3,
            "livesLost": 2,
            "tiersAvailable": 2,
            "levelUpTier": 3,
        },
        "turn-4": {
            "name": "Turn 4",
            "id": "turn-4",
            "index": 4,
            "foodShopSlots": 2,
            "animalShopSlots": 3,
            "livesLost": 2,
            "tiersAvailable": 2,
            "levelUpTier": 3,
        },
        "turn-5": {
            "name": "Turn 5",
            "id": "turn-5",
            "index": 5,
            "foodShopSlots": 2,
            "animalShopSlots": 4,
            "livesLost": 3,
            "tiersAvailable": 3,
            "levelUpTier": 4,
        },
        "turn-6": {
            "name": "Turn 6",
            "id": "turn-6",
            "index": 6,
            "foodShopSlots": 2,
            "animalShopSlots": 4,
            "livesLost": 3,
            "tiersAvailable": 3,
            "levelUpTier": 4,
        },
        "turn-7": {
            "name": "Turn 7",
            "id": "turn-7",
            "index": 7,
            "foodShopSlots": 2,
            "animalShopSlots": 4,
            "livesLost": 3,
            "tiersAvailable": 4,
            "levelUpTier": 5,
        },
        "turn-8": {
            "name": "Turn 8",
            "id": "turn-8",
            "index": 8,
            "foodShopSlots": 2,
            "animalShopSlots": 4,
            "livesLost": 3,
            "tiersAvailable": 4,
            "levelUpTier": 5,
        },
        "turn-9": {
            "name": "Turn 9",
            "id": "turn-9",
            "index": 9,
            "foodShopSlots": 2,
            "animalShopSlots": 5,
            "livesLost": 4,
            "tiersAvailable": 5,
            "levelUpTier": 6,
        },
        "turn-10": {
            "name": "Turn 10",
            "id": "turn-10",
            "index": 10,
            "foodShopSlots": 2,
            "animalShopSlots": 5,
            "livesLost": 4,
            "tiersAvailable": 5,
            "levelUpTier": 6,
        },
        "turn-11": {
            "name": "Turn 11+",
            "id": "turn-11",
            "index": 11,
            "foodShopSlots": 2,
            "animalShopSlots": 5,
            "livesLost": 5,
            "tiersAvailable": 6,
            "levelUpTier": 6,
        },
    },
}
# %%


################################################################################
#### Creating empty fields for pets and foods
################################################################################


def get_fields(d):
    """
    Recursive function to get all possible fields for the input dict

    """
    key_list = []
    for key, value in d.items():
        temp_key_list = [key]

        if type(value) == dict:
            temp_key_list.append(get_fields(value))

        key_list.append(temp_key_list)

    return key_list


def add_dummy_fields(fields, d):
    if d == "none":
        ### Sometimes there are dict or int datatype collisions in the given
        ### json information. This should probably be corrected.
        return
    if not fields or len(fields) == 0:
        return  # Exit early if fields is empty
    if type(fields[0]) == str:
        if len(fields) == 1:
            ### Break recursion condition
            d[fields[0]] = "none"
            return
        if type(fields[1]) == list:
            if fields[0] not in d:
                d[fields[0]] = {}

            for temp_fields in fields[1:]:
                add_dummy_fields(temp_fields, d[fields[0]])
    else:
        for temp_list in fields:
            add_dummy_fields(temp_list, d)


dummy_pet = {}
for temp_pet, value in data["pets"].items():
    temp_all_fields = get_fields(value)
    add_dummy_fields(temp_all_fields, dummy_pet)
data["pets"]["pet-none"] = dummy_pet

dummy_foods = {}
for temp_pet, value in data["foods"].items():
    temp_all_fields = get_fields(value)
    add_dummy_fields(temp_all_fields, dummy_foods)
data["foods"]["food-none"] = dummy_foods

# %%
