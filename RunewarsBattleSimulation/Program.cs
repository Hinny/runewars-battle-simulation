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
            Faction attacker = new DaqanLords();
            Faction defender = new UthukYllan();

            Battle battle = new Battle(attacker, defender);

            battle.ResolveBattle();

            Console.ReadKey();

        }
    }
}
