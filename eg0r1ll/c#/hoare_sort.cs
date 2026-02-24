using System;

namespace Program
{
    class Program
    {
        static void Hoare_sorting(int[] array)
        {
            foreach(int i in array)
            {
                Console.Write(i + " ");
            }
        }

        static void Main()
        {
            int[] array = {3, 4, 2, 1, 5};
            Hoare_sorting(array);
        }
    }
}
