package com.wimt_hackathon.SmartDocs.services;

import org.apache.tika.Tika;
import org.apache.tika.metadata.Metadata;
import java.io.InputStream;

public class DocumentProcessor {
    public static String extractText(InputStream documentStream) {
        try {
            Tika tika = new Tika();
            Metadata metadata = new Metadata();
            return tika.parseToString(documentStream, metadata);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}
