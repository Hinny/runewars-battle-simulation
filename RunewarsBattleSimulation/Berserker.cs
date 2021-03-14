namespace RunewarsBattleSimulation
{
    public class Berserker : UnitType
    {
        public Berserker(int startingAmount)
            : base(shape: Shape.triangle,
                   maxFigures: 16,
                   health: 1,
                   initiative: 2,
                   startingAmountofFigures: startingAmount) { }

    }
}