class Test extends Exception {}

class Main {
    public static void main (String[] args) throws java.lang.Exception
	{
		try{
            throw new Test();
        }
        catch(Test t){
            System.out.println("Got the Test Exception");
        }
        finally{
            System.out.println("Inside Final block");
        }
	}
}
