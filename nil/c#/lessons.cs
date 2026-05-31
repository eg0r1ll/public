int[,] array = new int[6,5];
Random random = new Random();
int sum = 0;
for(int i = 0;  i < array.GetLength(0); i++)
{
    for(int j = 0;  j < array.GetLength(1); j++)
    {
        array[i, j] = random.Next(50);
        sum += array[i, j];
    }
    
}
for (int i = 0; i < array.GetLength(0); i++)
{
    for (int j = 0; j < array.GetLength(1); j++)
    {
        Console.Write(array[i,j] + " ");
        
    }
    Console.WriteLine();
}
Console.WriteLine($"\nСумма всех элементов в массиве = {sum}");
Console.WriteLine($"\nСумма всех строк и столбцов = " + (array.GetLength(0) + array.GetLength(1))); 