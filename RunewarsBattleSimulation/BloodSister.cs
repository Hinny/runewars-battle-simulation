namespace RunewarsBattleSimulation
{
    public class BloodSister : UnitType
    {
        public BloodSister(int startingAmount)
            : base(shape: Shape.circle,
                   maxFigures: 8,
                   health: 1,
                   initiative: 2,
                   startingAmountofFigures: startingAmount) { }
    }
}