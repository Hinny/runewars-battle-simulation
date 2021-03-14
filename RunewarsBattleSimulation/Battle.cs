using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RunewarsBattleSimulation
{
    public class Battle
    {
        private readonly Player attacker;
        private readonly Player defender;
        private readonly FateDeck fateDeck = new FateDeck();
        private readonly BattleState battleState;

        public Battle(Player attacker, Player defender) {
            this.attacker = attacker;
            this.defender = defender;

        }

        public BattleResolution ResolveBattle() {
            Console.WriteLine("Resolve Battle!");
            foreach (UnitType unitType in attacker.GetUnitTypes()) {
                Console.WriteLine("Standing figures: " + unitType.GetStandingFigures().Count.ToString());
                unitType.DealDamage();
                Console.WriteLine("Damage Dealt!");
                Console.WriteLine("Standing figures: " + unitType.GetStandingFigures().Count.ToString());
                unitType.DealRout();
                Console.WriteLine("Rout Dealt!");
                Console.WriteLine("Standing figures: " + unitType.GetStandingFigures().Count.ToString());
            }


            BattleResolution battleResolution = TallyStrengh();
            return battleResolution;
        }

        private BattleResolution TallyStrengh() {
            // TODO
            BattleResolution battleResolution = new BattleResolution();
            return battleResolution;
        }
    }
}
