//Imports
import edu.cmu.sphinx.api.Configuration;
import edu.cmu.sphinx.api.LiveSpeechRecognizer;
import edu.cmu.sphinx.api.SpeechResult;
import java.io.IOException;
 
/**
 *
 * @author ex094
 */
public class VoiceLauncher {
    public static void main(String[] args) throws IOException {
        //Configuration Object
        Configuration configuration = new Configuration();
 
        // Set path to the acoustic model.
        configuration.setAcousticModelPath("resource:/edu/cmu/sphinx/models/en-us/en-us");
        // Set path to the dictionary.
        configuration.setDictionaryPath("/home/gokul/Desktop/sphinx test/TAR5391/5391.dic");
        // Set path to the language model.
        configuration.setLanguageModelPath("/home/gokul/Desktop/sphinx test/TAR5391/5391.lm");
 
 
        //Recognizer object, Pass the Configuration object
        LiveSpeechRecognizer recognize = new LiveSpeechRecognizer(configuration);
 
        //Start Recognition Process (The bool parameter clears the previous cache if true)
        recognize.startRecognition(true);
 
        //Creating SpeechResult object
        SpeechResult result;
 
        //Check if recognizer recognized the speech
        while ((result = recognize.getResult()) != null) {
 
            //Get the recognized speech
            String command = result.getHypothesis();
            System.out.println(command);
            //Match recognized speech with our commands
            if(command.equalsIgnoreCase("open file manager")) {
                System.out.println("File Manager Opened!");
            } else if (command.equalsIgnoreCase("close file manager")) {
                System.out.println("File Manager Closed!");
            } else if (command.equalsIgnoreCase("open browser")) {
                System.out.println("Browser Opened!");
            } else if (command.equalsIgnoreCase("close browser")) {
                System.out.println("Browser Closed!");
            }
        }
    }
}