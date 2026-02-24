using System;

namespace Program
{
	class Programm
	{
		static void Main()
		{   
            int[] array = {3, 2, 1, 4, 5};
            int temp;

            // bubble sort:
            for(int i = 0; i < array.Length; ++i)
            {
                for(int j = i; j < array.Length - i; ++j)
                {
                    if(array[i] > array[j])
                    {
                        temp = array[i];
                        array[i] = array[j];
                        array[j] = temp;
                    }
                }
            }

            // output:
            for(int i = 0; i < array.Length; ++i)
            {
                Console.Write($"{array[i]} ");
            }
            Console.WriteLine();
		}
	}
}
