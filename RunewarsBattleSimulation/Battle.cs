using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RunewarsBattleSimulation
{
    public class Battle
    {
        private readonly Faction attacker;
        private readonly Faction defender;
        
        public Battle(Faction attacker, Faction defender) {
            this.attacker = attacker;
            this.defender = defender;
        }

        public BattleResolution ResolveBattle() {
            Console.WriteLine("Resolve Battle!");

            BattleResolution battleResolution = TallyStrengh();
            return battleResolution;
        }

        private BattleResolution TallyStrengh() {
            string attackerType = attacker.GetType().ToString();
            string defenderType = defender.GetType().ToString();
            Console.WriteLine("Attacker Type: " + attackerType);
            Console.WriteLine("Defender Type: " + defenderType);
            BattleResolution battleResolution = new BattleResolution();
            return battleResolution;
        }
    }
}
