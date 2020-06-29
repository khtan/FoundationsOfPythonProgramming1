using System.Text;
using System.Collections.Generic;
using System.Linq;


namespace XUnitTests{
public static class Extensions1
{
    // IEnumerable does not have count before 4.7.1
    public static string ToString<T>(this IEnumerable<T> list, string desc = "list")
    {
        StringBuilder returnString = new StringBuilder(desc + "<" + typeof(T).Name + ">{");
        int numElements = list.Count();
        if (numElements == 0) returnString.Append("empty");
        else
        {
            for (int i = 0; i < numElements - 1; i++) { returnString.Append(list.ElementAt(i) + ","); }
            returnString.Append(list.ElementAt(numElements - 1));
        }
        returnString.Append("}");
        return returnString.ToString();
    }
} // class Extensions
} // namespace
