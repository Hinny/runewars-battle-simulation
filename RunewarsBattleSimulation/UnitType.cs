using System.Collections.Generic;

namespace RunewarsBattleSimulation
{
    public enum Shape
    {
        triangle,
        rectangle,
        hexagon,
        circle
    }

    public abstract class UnitType
    {

        protected List<Figure> figures;
        protected readonly string name;
        protected readonly Shape shape;
        protected readonly int maxFigures;
        protected readonly int health;
        protected readonly int initiative;
        protected bool hasActivated;

        protected UnitType(string name,
                           Shape shape,
                           int maxFigures,
                           int health,
                           int initiative,
                           int startingAmountofFigures) {
            this.name = name;
            this.shape = shape;
            this.maxFigures = maxFigures;
            this.health = health;
            this.initiative = initiative;

            hasActivated = false;

            figures = new List<Figure>();
            AddFigures(startingAmountofFigures);
        }
        public (int, Shape) Activate() {
            hasActivated = true;
            int numberOfStandingFigures = GetStandingFigures().Count;
            return (numberOfStandingFigures, shape);
        }

        public void AddFigures(int amount) {
            for (int i = 0; i < amount; i++) {
                if (figures.Count < maxFigures) {
                    Figure figure = new Figure();
                    figures.Add(figure);
                }
            }
        }

        public List<Figure> GetStandingFigures() {
            List<Figure> standingFigures = new List<Figure>();
            foreach (Figure figure in figures) {
                if (!figure.IsRouted()) {
                    standingFigures.Add(figure);
                }
            }
            return standingFigures;
        }

        public List<Figure> GetRoutedFigures() {
            List<Figure> routedFigures = new List<Figure>();
            foreach (Figure figure in figures) {
                if (figure.IsRouted()) {
                    routedFigures.Add(figure);
                }
            }
            return routedFigures;
        }

        public List<Figure> GetDamagedFigures() {
            List<Figure> damagedFigures = new List<Figure>();
            foreach (Figure figure in figures) {
                if (figure.IsDamaged()) {
                    damagedFigures.Add(figure);
                }
            }
            return damagedFigures;
        }

        public void DealDamage() {
            Figure selectedFigure = DecideBestCandidateToDamage();
            if (selectedFigure != null) {
                selectedFigure.Damage();
                if (selectedFigure.GetDamage() >= health) {
                    figures.Remove(selectedFigure);
                }
            }
            return;
        }

        public void DealRout() {
            Figure selectedFigure = DecideBestCandidateToRout();
            if (selectedFigure != null) {
                selectedFigure.Rout();
            }
            return;
        }

        private Figure DecideBestCandidateToDamage() {
            Figure bestCandidate = null;
            foreach (Figure figure in figures) {
                if (bestCandidate == null) {
                    bestCandidate = figure;
                } else if (figure.IsDamaged() && !bestCandidate.IsDamaged()) {
                    bestCandidate = figure;
                } else if (figure.GetDamage() < bestCandidate.GetDamage()) {
                    bestCandidate = figure;
                } else if ((figure.GetDamage() == bestCandidate.GetDamage()) && figure.IsRouted()) {
                    bestCandidate = figure;
                }
            }
            return bestCandidate;
        }

        private Figure DecideBestCandidateToRout() {
            Figure bestCandidate = null;
            List<Figure> standingFigures = GetStandingFigures();
            foreach (Figure figure in standingFigures) {
                if (bestCandidate == null) {
                    bestCandidate = figure;
                } else if (bestCandidate.IsDamaged() && !figure.IsDamaged()) {
                    bestCandidate = figure;
                } else if (bestCandidate.GetDamage() < figure.GetDamage()) {
                    bestCandidate = figure;
                }
            }
            return bestCandidate;
        }

        public class Figure
        {
            private int damage;
            private bool routed;

            public Figure() {
                damage = 0;
                routed = false;
            }

            public int Damage() {
                damage++;
                return damage;
            }

            public void Rout() {
                routed = true;
            }

            public int GetDamage() {
                return damage;
            }

            public bool IsDamaged() {
                if (damage > 0) {
                    return true;
                } else {
                    return false;
                }
            }

            public bool IsRouted() {
                return routed;
            }

        }

    }
}