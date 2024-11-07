package com.wimt_hackathon.SmartDocs.services;

import java.util.Map;

public class TemplateProcessor {
    private String template;

    public TemplateProcessor(String template) {
        this.template = template;
    }

    public String populateTemplate(Map<String, String> values) {
        for (Map.Entry<String, String> entry : values.entrySet()) {
            template = template.replace("{{" + entry.getKey() + "}}", entry.getValue());
        }
        return template;
    }
}
