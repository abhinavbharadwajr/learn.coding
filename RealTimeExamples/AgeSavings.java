package RealTimeExamples;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;
import java.util.Scanner;

public class AgeSavings {

    static int daysDifference(String date1, String date2) {
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        long daysDiff = 0L;

        try {
            LocalDate d1 = LocalDate.parse(date1, dtf);
            LocalDate d2 = LocalDate.parse(date2, dtf);

            daysDiff = ChronoUnit.DAYS.between(d1, d2);
        }
        catch (Exception e) {
            e.printStackTrace();
        }

        int result = (int)daysDiff;
        return result;
    }

    static int yearsDifference(String date1, String date2) {
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        long yearsDiff = 0L;

        try {
            LocalDate d1 = LocalDate.parse(date1, dtf);
            LocalDate d2 = LocalDate.parse(date2, dtf);

            yearsDiff = ChronoUnit.YEARS.between(d1, d2);
        }
        catch (Exception e) {
            e.printStackTrace();
        }

        int result = (int)yearsDiff;
        return result;
    }

    
    public static void main(String[] args) {

        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        System.out.println("\n Enter your Date of Birth (in dd-MM-yyyy format) : ");
        Scanner dobInput = new Scanner(System.in);
        String dob = dobInput.next();
        LocalDate dobDateFormat = LocalDate.parse(dob, dtf);
        
        int birthYear = dobDateFormat.getYear();
        System.out.println("\n Birth Year : "+birthYear);
        
        LocalDate currDateTime = LocalDate.now();
        String todaydate = currDateTime.format(dtf);
        
        int noofDaysOld = daysDifference(dob, todaydate);
        int noofYearsOld = yearsDifference(dob, todaydate);
                
        int savings = 0, yearCounter = birthYear;

        if((birthYear % 400 == 0) || ((birthYear % 4 == 0) && (birthYear % 100 != 0))) {
            savings = 366;
        } else {
            savings = 365;
        }

        for (int counter=1; counter<noofYearsOld; counter++) {

            if((yearCounter % 400 == 0) || ((yearCounter % 4 == 0) && (yearCounter % 100 != 0))) {
                savings = savings + (counter*366);
            }
            else {
                savings = savings + (counter*365);
            }
            yearCounter++;

        }

        System.out.println("\n You are "+noofDaysOld+" Days Old!");
        System.out.println("\n You are "+noofYearsOld+" Years Old!");
        System.out.println("\n Your Total estimated Savings would be : Rs."+savings);
        
        dobInput.close();
    }
}
