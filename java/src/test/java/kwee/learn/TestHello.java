package kwee.learn;

import org.junit.Assert;
import org.junit.Test;
import org.junit.Ignore;
import junit.runner.Version;
import static java.lang.System.getenv;
@Ignore("Enable to test for failing test")
public class TestHello{
    @Test
    public void passingTest(){
    }

    @Test
    public void failingTest(){
        Assert.fail("a failing test");
    }
    @Test
    public void checkVersions(){
        Assert.assertEquals("4.12", Version.id());
        Assert.assertEquals("C:\\Program Files\\Java\\jdk-11.0.1", getenv("JAVA_HOME"));
        // Assert.assertEquals("C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2019.3\\lib", getenv("JUNIT_HOME"));
        Assert.assertEquals(null, getenv("CLASSPATH"));

    }
}
