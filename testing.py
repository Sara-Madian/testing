import streamlit as st
 
def show_notes(disease):
    notes = {
        "Multiple myeloma": "Malignant neoplasm of plasma cells, which are a type of white blood cell. It often affects the bones, causing pain, fractures, and bone lesions. Most patients are males,Present between 35 and 70 years of age. Lab investigation: Bence-Jones protein can be detected in the patient's urine, which causes it to be foamy. Radiographically: *Mandible posterior body, *Well-defined punched out lesion, *Multiple unilocular radiolucency, *Causing Loss of Lamina Dura. Note that: MRI is more sensitive than X-rays for detecting bone marrow involvement and soft tissue masses.",
        "Langerhans Cell Histiocytosis": "A rare disease involving the proliferation of Langerhans cells, which are a type of immune cell. manifests as Multiple eosinophilic granulomas in the jaws, often affecting children with Male predilection.Symptoms range from isolated bone lesions to multisystem disease; Unifocal, multifocal unisystem, and multifocal multisystem. Radiographically:*Mandible posterior body and ramus, *Well-defined punched out lesion, *Multiple unilocular radiolucency, *A hole within a hole sign; double contour or beveled edge appearance may be seen due to asymmetrical involvement of the inner and outer tables. Note that: Lesions within the alveolar processes have an epicenter in the mid-root regions of the teeth. The bone destruction progresses in oval or round shape until the alveolar process appears scooped out.",
        "Leukemia": "Malignant neoplasm of hematopoietic stem cells in which malignant cells are disseminated throughout the bone marrow via the circulating blood. It has a bimodal age distribution, in very young patients and very old patients. Radiographically: *Areas of developing teeth, *Bilaterally poorly defined lesion, *Radiolucent, with generalized rarefaction of  bone , *Does not cause expansion of bone. Note that: The lesions may involve the periodontal ligament space causing nonconcentric widening.",
        "Lymphoma": "Malignant neoplasms of lymphocytes. Arise within lymph nodes; extranodal sites, such as bone, skin, gastrointestinal mucosa, and tonsils. Radiographically: *Maxilla, *Poorly defined invasive borders, *Radiolucent, *Round or multiloculated. Note that: Lymphoma has a propensity to grow into the periodontal ligament space of erupted teeth.",
        "Burkitt lymphoma": "A high-grade B-cell lymphoma with a strong male predilection. African Burkitt lymphoma affects young children involving one jaw or both, primarily affecting the posterior parts of the jaws. American Burkitt lymphoma affects adolescents and young adults, they are more likely to affect the abdominal viscera and testes.Radiographically: *Posterior parts of the jaws, *Poorly defined radiolucency, *The cortex of the IAN is lost, *“Sunray” type of speculation.",
        "Metastatic diseases": "Cancers that have spread from their original site to the bone, causing lesions, Metastatic disease that involves the jaws usually comes from distant primary lesion, usually located anatomically inferior to the clavicles. Radiographically: *The posterior mandible is most commonly affected given the rich vascular supply to this area of the bone, *Poorly defined peripheries, *Radiolucent except metastatic tumors from breast and prostate that may appear as radiopaque lesions, *Non concentric widening of the PDL.",
        "Squamous odontogenic tumor": "A rare benign odontogenic tumor that can cause lesions in the jawbone. Affects a wide age group. Radiographically: *Maxilla = mandible on lateral root surface , *Well-defined, *Unilocular radiolucency , *Triangular or semilunar resembling vertical bone loss.",
        "Multiple Keratocysts": "Multiple cysts that occur in the jawbone, often associated with genetic syndromes called Gorlin Goltz syndrome (Nevoid Basal Cell Carcinoma). Such syndrome characterised by Multiple basal cell carcinomas of the skin, Skeletal abnormalities such as bifid ribs, vertebral fusion, and mild prognathism, and Multiple OKCs.",
        "Cherubism (bilateral)": "Inherited developmental abnormality. Affecting early childhood (2-6 yrs) with male predilection. causing Bilateral enlargement of jaws. manifests as Raised to heaven eyes. Radiographically: *Mandible is more affected, *Well-defined, corticated, *Multilocular radiolucency “soap bubble” , *Displacement of  maxillary sinus, ramus and teeth in mesial direction.",
        "Paget’s disease of bone": "A chronic bone disorder that can cause enlarged and weakened bones, leading to deformities and pain. characterized by resorption of the bone followed by the formation of disorganized woven abnormal bone. Affecting people older than 50 years with male predilection. Causing aveolar ridge enlargement (leontiasis ossia) leading to tooth spacing and an abnormal occlusal pattern. Lab Investigation: > Increased serum alkaline phosphatase. > Increased urinary hydroxyproline level. > Normal serum calcium and phosphorous level. Radiographically: begins Radiolucent >> Ground Glass Appearance >> Cotton Wool Appearance. ",
        "Central Giant Cell Granuloma": "A benign bone lesion that can cause swelling and bone destruction. Affecting anterior part of the jaw, especially the mandible (mesial to the first molar in the mandible, mesial to the canine in the maxilla). Has female predilection under 30 years of age. Radiographically: *Anterior of the jaws, *Well-defined, not corticated, *Unilocular or multilocular radiolucency, *Displacement and resorption of the roots",
        "Hyperparathyroidism": "A condition characterized by overactivity of the parathyroid glands, which can lead to bone changes and lesions. Brown tumor of Hyperparathyroidism characterized Radiographically as:*Mandible is more affected, *Well-defined, *Unilocular or multilocular radiolucency, *Solitary but are often multiple. ",
        "Osseous Dysplasia": "A reactional process located in the periapical region of jaws. Characterized by replacement of normal bone by fibrous tissue and metaplastic bone. Associated with vital teeth or in edentulous areas. It is asymptomatic lesion. Radiographically: *Periapical to vital tooth, *Well-defined corticated, *Radiolucent >> Mixed >> Radiopaque, *Large lesions may cause expansion.",
        "Gorham-Stout Disease": "Named Vanishing bone disease or disappearing bone disease. A rare bone disorder that is characterized by progressive bone loss caused by infiltration of venous and lymphatic tissue in affected areas.Unknown cause with no standard treatment protocol. Radiographically: *Mostly bilateral, *Poorly defined borders, *Radiolucent, *Floating teeth, cortex destruction.",
        "Osteomyelitis": "Infection of medullary part of bone, spreads via the bloodstream or from nearby areas of infection. Has a strong male predilection. Note that: To be visible by conventional radiography, a lesion must have resorbed or demineralized approximately 60% of the bone. Radiographically: *The posterior body of the mandible, *Poorly defined borders, *Unilocular radiolucency (Moth-eaten) in early stages, *Periosteal new bone formation (onion skin) appearance in Garre's osteomyelitis.",
        "Periapical granuloma": "Localized inflammatory lesions caused by Chronic dental infection or irritation. Asymptomatic lesion. Radiographically: *Apex of non-vital tooth, *Well-defined corticated, *Unilocular radiolucency, *Causes widening of PDL space.",
        "Radicular cyst": "A cyst that forms at the root of a non-vital tooth, often as a result of chronic pulpitis. Asymptomatic unless infected. Causes Cortical expansion. Radiographically: *Apex of non-vital tooth (maxilla), *Well-defined corticated, *Unilocular radiolucency, *Hydraulic shape.",
        "Other benign odontogenic cysts or tumors": "Includes various benign lesions originating from tooth-forming tissues.",
        "Early stage of osseous dysplasia": "A reactional process located in the periapical region of jaws. Characterized by replacement of normal bone by fibrous tissue and metaplastic bone. Associated with vital teeth or in edentulous areas. It is asymptomatic lesion. Radiographically: *Periapical to vital tooth, *Well-defined corticated, *Radiolucent >> Mixed >> Radiopaque, *Large lesions may cause expansion.",
        "Early stage of ossifying fibroma": "Ossifying fibroma consists of fibrous tissue containing variable amounts of mineralized material. It originates from the periodontal ligament. Therefore, it produces cementum and osteoid material. Radiographically: *Posterior mandible, *Well-defined corticated, *Radiolucent >> Mixed >> Radiopaque, *Maxillary lesions are more aggressive.",
        "Dentigerous cyst": "A type of odontogenic cyst associated with the crown of an unerupted tooth. Attaches to the cementoenamel junction. Radiographically: *Pericoronal, mandibular 3rd molar, *Well-defined corticated, *Unilocular radiolucency, *Displace or resorb adjacent teeth.",
        "Unicystic ameloblastoma": "A type of ameloblastoma that presents as a single cystic lesion related to the crown of unerupted tooth Apical to the cementoenamel junction. Radiographically: *Pericoronal, mandibular 3rd molar, *Well-defined corticated, *Unilocular radiolucency, *Displace or resorb adjacent teeth.",
        "Odontogenic Keratocyst": "An odontogenic cyst characterized by a unique lining and aggressive behavior. Causes Anteroposterior expansion of the jaws. Have a great propensity for recurrence. Manifests as Multifocal or Focal Unilocular or Multilocular and may be associated with the crown of unerupted tooth. Radiographically: *Mandible posterior body and ramus, *Well-defined corticated, *Unilocular or multilocular radiolucency, *Displace or resorb adjacent teeth. ",
        "Ameloblastic fibroma": "A benign tumor composed of both dental epithelium and mesenchymal tissue. Affecting Young males in most cases. Mostly associated with Unerupted tooth. Radiographically: *Mandible posterior body and ramus, *Well-defined corticated, *Unilocular or multilocular radiolucency, *Unerupted tooth is associated in 75% of cases.",
        "Lateral Inflammatory cyst": "An inflammatory cyst that develops along the lateral aspect of the roots of non-vital teeth. Radiographically: *Lateral root surface, *Well-defined corticated, *Unilocular radiolucency, *non-vital tooth.",
        "Lateral developmental cyst": "A type of developmental cyst located along the lateral aspect of the roots of vital teeth.Radiographically: *Lateral root surface, *Well-defined corticated, *Unilocular radiolucency, *Vital tooth.",
        "Traumatic bone cyst": "Simple bone cyst (SBC) is not a true cyst! It may be empty or contain a small amount of blood or serosanguinous fluid. Radiographically: *Mandible posterior body, *Well-defined corticated, *Unilocular radiolucency, *Periphery scallops around the roots.",
        "Median Palatine cyst": "A developmental cyst located in the midline of the hard palate.",
        "Nasopalatine cyst": "A developmental cyst located in the midline of the nasopalatine foramen. Radiographically: *Midline behind the two central incisors, *Well-defined corticated, *Unilocular radiolucency, *Heart shape",
        "Globulomaxillary cyst": "A cyst located between the roots of the maxillary lateral incisor and canine teeth. Teeth are vital. Discovered on routine radiological examination. Radiographically: *Inverted pear-shaped, *Well-defined corticated, *Unilocular radiolucency, *Divergence of the roots.",
        "Vascular malformation": "Congenital high-flow vascular anomalies. Causes life-threatening hemorrhage either spontaneously or after oral surgeries. Radiographically: *Pericoronal, mandibular 3rd molarMandible, *Well-defined corticated, *Unilocular radiolucency, *Widening of the mandibular canal. Note that: Angiography is very important for diagnosis.",
        "Schwannoma": "A tumor of the Schwann cells that can occur in the jawbone. It is the most common tumor of peripheral nerves. Most schwannomas are solitary. Multiple schwannomas are characteristic of neurofibromatosis. Radiographically: *Mandible, *Well-defined, *Round unilocular radiolucency, *Displace adjacent structures without direct invasion. Note that MRI is the gold standard for diagnosis.",
        "Neurofibroma": "A benign nerve sheath tumor that can occur in the jawbone. Usually solitary and sporadic. Could be associated with neurofibromatosis type I. Radiographically: *Mandible, *Well-defined, *Unilocular radiolucency, *Fusiform appearance.",
        "Static bone cyst": "STAFNE BONE DEFECT is a depression within the lingual surface of the mandible resulting from growth of the adjacent submandibular salivary gland. Radiographically: *Mandible inferior to IAC, *Well-defined corticated, *Unilocular radiolucency, *Continuous with the inferior cortex.",
        "Plasmacytoma": "A solitary plasma cell tumor that can occur in bone or soft tissue. it is the solitary counterpart of multiple myeloma. Most patients are males, Present between 35 and 70 years of age. Lab investigation: Bence-Jones protein can be detected in the patient's urine, which causes it to be foamy. Radiographically: *Mandible posterior body, *Well-defined punched out lesion, *Unilocular radiolucency, *Causing Loss of Lamina Dura. Note that: MRI is more sensitive than X-rays for detecting bone marrow involvement and soft tissue masses.",
        "Chronic periapical abscess": "A localized infection at the apex of a tooth root that persists over time.",
        "Malignant odontogenic tumors": "Cancers arising from the odontogenic tissues with aggressive behavior.",
        "Glandular odontogenic cyst": "A cyst with glandular epithelial lining, often found in the jawbone. Has an aggressive behavior and a tendency to recur after surgery. More common in males in the fifth decade of life. Radiographically: *Anterior of the mandible, *Well-defined corticated border, *Unilocular or multilocular radiolucency, *Displacement of the roots.",
        "Ameloblastoma": "A benign locally aggressive odontogenic tumor causing Buccal and lingual expansion of the jaw. Has different types as solid ameloblastoma, unicyctic ameloblastoma, desmoplastic ameloblastoma and the malignant variant. Radiographically the solid variant appears as: *Mandible molar area and ascending ramus, *Well-defined corticated, *Unilocular radiolucent cavity, multilocular  with partial division by coarse septa ,multilocular radiolucent cavities giving honey-combed or soap bubble appearance, *Egg-shell crackling of the bone due to excessive bone expansion and resorption",
        "Odontogenic myxoma": "A rare, benign tumor of the jaw characterized by a myxoid stroma. It may cause Buccal or lingual expansion. Has gelatinous consistency. It has a high rate of recurrence because it has no capsule. Radiographically: *Mandibular molar area, *Irregular scalloped margins, *Multilocular radiolucency, *Tennis racket appearance.",
        "Central odontogenic fibroma": "A benign tumor with fibrous tissue that originates in the jawbone. Radiographically: *The apical part of an erupted tooth, *Well-defined, *Unilocular or multilocular radiolucency, *Root resorption.",
        "Central hemangioma": "A benign vascular tumor located within the jawbone. It is the intraosseous type of hemangiomas. Radiographically: *The mandible posterior area, *Well-defined corticated, *Multilocular radiolucency, *Root resorption or displacement.",
        "Aneurysmal bone cyst": "A benign bone lesion with blood-filled cystic spaces. More common in females Younger than 30 years old. Radiographically: *The mandible posterior area, *Well-defined corticated, *Multilocular radiolucency, *Circular or hydraulic in shape.",
    }
    st.write(notes.get(disease, "No information available."))

def lesion_diagnosis():
    st.title("Lesion Differential Diagnosis")

    lesion_type = st.selectbox("Select the lesion type:", ["Focal", "Multifocal"])

    if lesion_type == "Multifocal":
        st.write("The lesion differential diagnosis could be:")

        diseases = [
            "Multiple myeloma",
            "Langerhans Cell Histiocytosis",
            "Leukemia",
            "Lymphoma",
            "Burkitt lymphoma",
            "Metastatic diseases",
            "Squamous odontogenic tumor",
            "Multiple Keratocysts",
            "Cherubism (bilateral)",
            "Paget’s disease of bone",
            "Central Giant Cell Granuloma",
            "Hyperparathyroidism",
            "Osseous Dysplasia",
            "Gorham-Stout Disease",
            "Osteomyelitis"
        ]

        for disease in diseases:
            if st.button(disease):
                show_notes(disease)

    elif lesion_type == "Focal":
        locularity = st.selectbox("Is the lesion Unilocular or Multilocular?", ["Unilocular", "Multilocular"])

        if locularity == "Unilocular":
            border = st.selectbox("Is the lesion Well-defined or Ill-defined?", ["Well-defined", "Ill-defined"])

            if border == "Well-defined":
                location_type = st.selectbox("Is the lesion Tooth-related, Has a Specific site, or With No specific site?", ["Tooth-related", "Specific site", "No specific site"])

                if location_type == "Tooth-related":
                    tooth_location = st.selectbox("Is the lesion Periapical, Pericoronal, or Interradicular?", ["Periapical", "Pericoronal", "Interradicular"])

                    if tooth_location == "Periapical":
                        st.write("The lesion could be:")
                        lesions = [
                            "Periapical granuloma",
                            "Radicular cyst",
                            "Other benign odontogenic cysts or tumors",
                            "Early stage of osseous dysplasia",
                            "Early stage of ossifying fibroma"
                        ]

                        for lesion in lesions:
                            if st.button(lesion):
                                show_notes(lesion)

                    elif tooth_location == "Pericoronal":
                        st.write("The lesion could be:")
                        lesions = [
                            "Dentigerous cyst",
                            "Unicystic ameloblastoma",
                            "Odontogenic Keratocyst",
                            "Ameloblastic fibroma"
                        ]

                        for lesion in lesions:
                            if st.button(lesion):
                                show_notes(lesion)

                    elif tooth_location == "Interradicular":
                        st.write("The lesion could be:")
                        lesions = [
                            "Lateral Inflammatory cyst",
                            "Lateral developmental cyst",
                            "Traumatic bone cyst",
                            "Squamous odontogenic tumor"
                        ]

                        for lesion in lesions:
                            if st.button(lesion):
                                show_notes(lesion)

                elif location_type == "Specific site":
                    site = st.selectbox("Is the lesion in the Anterior maxilla, Within the inferior alveolar nerve, or Below the inferior alveolar nerve?", ["Anterior maxilla", "Within the inferior alveolar nerve", "Below the inferior alveolar nerve"])

                    if site == "Anterior maxilla":
                        st.write("The lesion could be:")
                        lesions = [
                            "Median Palatine cyst",
                            "Nasopalatine cyst",
                            "Globulomaxillary cyst"
                        ]

                        for lesion in lesions:
                            if st.button(lesion):
                                show_notes(lesion)

                    elif site == "Within the inferior alveolar nerve":
                        st.write("The lesion could be:")
                        lesions = [
                            "Vascular malformation",
                            "Schwannoma",
                            "Neurofibroma"
                        ]

                        for lesion in lesions:
                            if st.button(lesion):
                                show_notes(lesion)

                    elif site == "Below the inferior alveolar nerve":
                        st.write("The lesion could be:")
                        lesions = ["Static bone cyst"]

                        for lesion in lesions:
                            if st.button(lesion):
                                show_notes(lesion)

                elif location_type == "No specific site":
                    st.write("The lesion could be:")
                    lesions = [
                        "Plasmacytoma",
                        "Hyperparathyroidism",
                        "Paget’s disease of bone",
                        "Leukemia",
                        "Lymphoma",
                        "Metastatic diseases"
                    ]

                    for lesion in lesions:
                        if st.button(lesion):
                            show_notes(lesion)

            elif border == "Ill-defined":
                st.write("The lesion could be:")
                lesions = [
                    "Chronic periapical abscess",
                    "Osteomyelitis",
                    "Malignant odontogenic tumors"
                ]

                for lesion in lesions:
                    if st.button(lesion):
                        show_notes(lesion)

        elif locularity == "Multilocular":
            border = st.selectbox("Is the lesion Well-defined or Ill-defined?", ["Well-defined", "Ill-defined"])

            if border == "Ill-defined":
                st.write("The lesion could be:")
                lesions = ["Malignant odontogenic tumors"]

                for lesion in lesions:
                    if st.button(lesion):
                        show_notes(lesion)

            elif border == "Well-defined":
                location = st.selectbox("Is the lesion in the Anterior of the jaw or Posterior of the jaw?", ["Anterior", "Posterior"])

                if location == "Anterior":
                    st.write("The lesion could be:")
                    lesions = [
                        "Central Giant Cell Granuloma",
                        "Glandular odontogenic cyst"
                    ]

                    for lesion in lesions:
                        if st.button(lesion):
                            show_notes(lesion)

                elif location == "Posterior":
                    st.write("The lesion could be:")
                    lesions = [
                        "Ameloblastoma",
                        "Odontogenic Keratocyst",
                        "Odontogenic myxoma",
                        "Central odontogenic fibroma",
                        "Central hemangioma",
                        "Aneurysmal bone cyst",
                        "Ameloblastic fibroma"
                    ]

                    for lesion in lesions:
                        if st.button(lesion):
                            show_notes(lesion)

    else:
        st.write("Invalid input. Please specify 'Focal' or 'Multifocal'.")

# Main function to run the Streamlit app
def main():
    lesion_diagnosis()

if __name__ == "__main__":
    main()
