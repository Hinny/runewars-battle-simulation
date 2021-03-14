using System.Collections.Generic;

namespace RunewarsBattleSimulation
{
    public class Footman : UnitType
    {
        public Footman(int startingAmount)
            : base("Footman", Shape.triangle, 16, 1, 3, startingAmount) { }

    }
}
