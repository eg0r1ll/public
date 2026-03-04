static object print(object word)
{
    Console.WriteLine(word);
    return word;
}

static double CaculateAvarage(int[] arr)
{
    double sum = 0;
    for (int i = 0; i < arr.Length; i++)
    {
        sum += arr[i];
    }

    return sum / arr.Length;
}

static string GetGradeDescription(double avg)
{

    if (avg >= 4.5)
        return "Отлично";
    else if (avg < 4.5 && avg >= 3.5)
        return "Хорошо";
    else
        return "Плохо";

}


Console.WriteLine("Введите сколько у вас оценок ");
int length = Convert.ToInt32(Console.ReadLine());
int[] array = new int[length];
Console.WriteLine("Введите все оценки  ");
for (int i = 0; i < array.Length; i++)
{
    int temp = Convert.ToInt32(Console.ReadLine());
    if (temp >= 2 && temp <= 5)
    {
        array[i] = temp;
    }
    else
    {
        Console.WriteLine("Некоректный ввод оценок"); i--;
        continue;
    }

}
Console.Clear();
print($"Ваш средний балл: {CaculateAvarage(array):F1}");
print(GetGradeDescription(CaculateAvarage(array)));