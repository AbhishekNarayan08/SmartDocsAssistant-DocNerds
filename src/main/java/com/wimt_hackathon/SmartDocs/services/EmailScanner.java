package com.wimt_hackathon.SmartDocs.service;

import javax.mail.*;
import javax.mail.internet.*;
import java.util.Properties;

public class EmailScanner {
    public static void scanEmails() {
        Properties props = new Properties();
        props.put("mail.store.protocol", "imaps");

        try {
            Session session = Session.getDefaultInstance(props, null);
            Store store = session.getStore("imaps");
            store.connect("imap.emailprovider.com", "your-email@example.com", "your-password");

            Folder inbox = store.getFolder("INBOX");
            inbox.open(Folder.READ_ONLY);

            for (Message message : inbox.getMessages()) {
                if (message.getContentType().contains("multipart")) {
                    Multipart multipart = (Multipart) message.getContent();
                    for (int i = 0; i < multipart.getCount(); i++) {
                        BodyPart bodyPart = multipart.getBodyPart(i);
                        if (Part.ATTACHMENT.equalsIgnoreCase(bodyPart.getDisposition())) {
                            // Save attachment for further processing
                            String fileName = bodyPart.getFileName();
                            InputStream stream = bodyPart.getInputStream();
                            // Process the file stream here
                        }
                    }
                }
            }
            inbox.close(false);
            store.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
