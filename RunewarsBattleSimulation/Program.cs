using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RunewarsBattleSimulation
{
    class Program
    {
        static void Main(string[] args) {
            Player attacker = CreateDaqanPlayer();
            Player defender = CreateUthukPlayer();

            Battle battle = new Battle(attacker, defender);

            battle.ResolveBattle();

            Console.ReadKey();

        }

        static Player CreateDaqanPlayer() {
            List<UnitType> unitTypes = new List<UnitType>();
            unitTypes.Add(new Footman(3));
            return new Player(unitTypes);
        }
        static Player CreateUthukPlayer() {
            List<UnitType> unitTypes = new List<UnitType>();
            return new Player(unitTypes);
        }
    }
}
