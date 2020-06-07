package kwee.learn;
import static org.junit.jupiter.api.Assertions.fail;
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Disabled;
import static java.lang.System.getenv;

import org.junit.jupiter.api.Test;
import junit.runner.Version;

@Disabled("Enable to test for failing tests")
public class TestHelloJunit5{
    @Test
    public void passingTest(){
    }
    @Test
    public void failingTest(){
        fail("a failing test");
    }

    @Test
    public void checkVersions(){
        assertEquals("4.12", Version.id());
        assertEquals("C:\\Program Files\\Java\\jdk-11.0.1", getenv("JAVA_HOME"));
        assertEquals("C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2019.3\\lib", getenv("JUNIT_HOME"));
        assertEquals(null, getenv("CLASSPATH"));
    }

}
