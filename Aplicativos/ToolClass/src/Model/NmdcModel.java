package Model;

/**
 *
 * Maycol Pazmiño
 * 
 */
public class NmdcModel {
    
    private String idNMDC;
    private String description;
    private String OD;
    private String ID;
    private String material;
    private String comany;
    private String weigth;
    private String length;
    private String conection_type;
    private String image;

    public NmdcModel(String idNMDC, String description, String OD, String ID, String material, String comany, String weigth, String length, String conection_type, String image) {
        this.idNMDC = idNMDC;
        this.description = description;
        this.OD = OD;
        this.ID = ID;
        this.material = material;
        this.comany = comany;
        this.weigth = weigth;
        this.length = length;
        this.conection_type = conection_type;
        this.image = image;
    }

    public NmdcModel() {
        this.idNMDC = idNMDC;
    }

    public String getIdNmdc() {
        return idNMDC;
    }

    public String getDescription() {
        return description;
    }

    public String getOD() {
        return OD;
    }

    public String getID() {
        return ID;
    }

    public String getMaterial() {
        return material;
    }

    public String getComany() {
        return comany;
    }

    public String getWeigth() {
        return weigth;
    }

    public String getLength() {
        return length;
    }

    public String getConection_type() {
        return conection_type;
    }

    public String getImage() {
        return image;
    }      
}
