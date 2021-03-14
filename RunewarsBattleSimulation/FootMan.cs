namespace RunewarsBattleSimulation
{
    public class Footman : UnitType
    {
        public Footman(int startingAmount)
            : base(shape: Shape.triangle,
                   maxFigures: 16,
                   health: 1,
                   initiative: 3,
                   startingAmountofFigures: startingAmount) { }

    }
}
