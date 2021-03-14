namespace RunewarsBattleSimulation
{
    public class Knight : UnitType
    {
        public Knight(int startingAmount)
            : base(shape: Shape.rectangle,
                   maxFigures: 8,
                   health: 2,
                   initiative: 2,
                   startingAmountofFigures: startingAmount) { }

    }
}