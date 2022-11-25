class Tester
{
	public static void main (String[] args) throws java.lang.Exception
	{
		try{
			int c[] = {1};
			System.out.println(c.length);
            c[1] = 142;
            System.out.println("c="+c[1]);
            int a = args.length;
            System.out.println("a="+a);
            int b = 8 / a;
		}
        catch (ArithmeticException e){
            System.out.println("Dived by 0 : "+e);
        }
        catch(ArrayIndexOutOfBoundsException e){
            System.out.println("Array Index oob:"+e);
        }
        System.out.println("After try/catch blocks.");
	}
}