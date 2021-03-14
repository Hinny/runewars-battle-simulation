using System.Collections.Generic;

namespace RunewarsBattleSimulation
{
    public class Player
    {
        private List<UnitType> unitTypes;

        public Player(List<UnitType> unitTypes) {
            this.unitTypes = unitTypes;
        }

        public List<UnitType> GetUnitTypes() {
            return unitTypes;
        }


    }
}