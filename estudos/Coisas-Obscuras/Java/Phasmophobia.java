import java.util.*;


enum Evidencia {
    EMF5,
    SPIRIT_BOX,
    ULTRAVIOLET,
    GHOST_WRITING,
    DOTS,
    FREEZING,
    ORB
}


abstract class Fantasma {
    protected String nome;
    protected Set<Evidencia> evidencias;

    public Fantasma(String nome, Evidencia... evidencias) {
        this.nome = nome;
        this.evidencias = new HashSet<>(Arrays.asList(evidencias));
    }

    public String getNome() {
        return nome;
    }

    public Set<Evidencia> getEvidencias() {
        return evidencias;
    }

    public boolean combinaCom(Set<Evidencia> evidenciasJogador) {
        return evidencias.containsAll(evidenciasJogador);
    }

    public abstract void habilidade();
}
class Spirit extends Fantasma {
    public Spirit() {
        super("Spirit", Evidencia.EMF5, Evidencia.SPIRIT_BOX, Evidencia.GHOST_WRITING);
    }
    public void habilidade() { System.out.println("Incenso dura mais."); }
}

class Wraith extends Fantasma {
    public Wraith() {
        super("Wraith", Evidencia.EMF5, Evidencia.SPIRIT_BOX, Evidencia.DOTS);
    }
    public void habilidade() { System.out.println("Não pisa em sal."); }
}

class Phantom extends Fantasma {
    public Phantom() {
        super("Phantom", Evidencia.SPIRIT_BOX, Evidencia.ULTRAVIOLET, Evidencia.DOTS);
    }
    public void habilidade() { System.out.println("Some em fotos."); }
}

class Poltergeist extends Fantasma {
    public Poltergeist() {
        super("Poltergeist", Evidencia.SPIRIT_BOX, Evidencia.ULTRAVIOLET, Evidencia.GHOST_WRITING);
    }
    public void habilidade() { System.out.println("Joga objetos."); }
}

class Banshee extends Fantasma {
    public Banshee() {
        super("Banshee", Evidencia.ULTRAVIOLET, Evidencia.ORB, Evidencia.DOTS);
    }
    public void habilidade() { System.out.println("Foca em um jogador."); }
}

class Jinn extends Fantasma {
    public Jinn() {
        super("Jinn", Evidencia.EMF5, Evidencia.ULTRAVIOLET, Evidencia.FREEZING);
    }
    public void habilidade() { System.out.println("Mais rápido com energia."); }
}

class Mare extends Fantasma {
    public Mare() {
        super("Mare", Evidencia.SPIRIT_BOX, Evidencia.GHOST_WRITING, Evidencia.ORB);
    }
    public void habilidade() { System.out.println("Mais forte no escuro."); }
}

class Revenant extends Fantasma {
    public Revenant() {
        super("Revenant", Evidencia.ORB, Evidencia.GHOST_WRITING, Evidencia.FREEZING);
    }
    public void habilidade() { System.out.println("Muito rápido ao ver jogador."); }
}

class Shade extends Fantasma {
    public Shade() {
        super("Shade", Evidencia.EMF5, Evidencia.GHOST_WRITING, Evidencia.FREEZING);
    }
    public void habilidade() { System.out.println("Tímido."); }
}

class Demon extends Fantasma {
    public Demon() {
        super("Demon", Evidencia.ULTRAVIOLET, Evidencia.GHOST_WRITING, Evidencia.FREEZING);
    }
    public void habilidade() { System.out.println("Ataca frequentemente."); }
}

class Yurei extends Fantasma {
    public Yurei() {
        super("Yurei", Evidencia.ORB, Evidencia.FREEZING, Evidencia.DOTS);
    }
    public void habilidade() { System.out.println("Drena sanidade."); }
}

class Oni extends Fantasma {
    public Oni() {
        super("Oni", Evidencia.EMF5, Evidencia.FREEZING, Evidencia.DOTS);
    }
    public void habilidade() { System.out.println("Muito ativo."); }
}

class Yokai extends Fantasma {
    public Yokai() {
        super("Yokai", Evidencia.SPIRIT_BOX, Evidencia.ORB, Evidencia.DOTS);
    }
    public void habilidade() { System.out.println("Reage à voz."); }
}

class Hantu extends Fantasma {
    public Hantu() {
        super("Hantu", Evidencia.ULTRAVIOLET, Evidencia.ORB, Evidencia.FREEZING);
    }
    public void habilidade() { System.out.println("Depende da temperatura."); }
}

class Goryo extends Fantasma {
    public Goryo() {
        super("Goryo", Evidencia.EMF5, Evidencia.ULTRAVIOLET, Evidencia.DOTS);
    }
    public void habilidade() { System.out.println("Aparece só em câmera."); }
}

class Myling extends Fantasma {
    public Myling() {
        super("Myling", Evidencia.EMF5, Evidencia.ULTRAVIOLET, Evidencia.GHOST_WRITING);
    }
    public void habilidade() { System.out.println("Silencioso."); }
}

class Onryo extends Fantasma {
    public Onryo() {
        super("Onryo", Evidencia.SPIRIT_BOX, Evidencia.ORB, Evidencia.FREEZING);
    }
    public void habilidade() { System.out.println("Fogo o afasta."); }
}

class TheTwins extends Fantasma {
    public TheTwins() {
        super("The Twins", Evidencia.EMF5, Evidencia.SPIRIT_BOX, Evidencia.FREEZING);
    }
    public void habilidade() { System.out.println("Atacam em dupla."); }
}

class Raiju extends Fantasma {
    public Raiju() {
        super("Raiju", Evidencia.EMF5, Evidencia.ORB, Evidencia.DOTS);
    }
    public void habilidade() { System.out.println("Usa eletrônicos."); }
}

class Obake extends Fantasma {
    public Obake() {
        super("Obake", Evidencia.EMF5, Evidencia.ULTRAVIOLET, Evidencia.ORB);
    }
    public void habilidade() { System.out.println("Digitais raras."); }
}

class Mimic extends Fantasma {
    public Mimic() {
        super("The Mimic", Evidencia.SPIRIT_BOX, Evidencia.ULTRAVIOLET, Evidencia.FREEZING);
    }
    public void habilidade() { System.out.println("Imita outros."); }
}

class Moroi extends Fantasma {
    public Moroi() {
        super("Moroi", Evidencia.SPIRIT_BOX, Evidencia.GHOST_WRITING, Evidencia.FREEZING);
    }
    public void habilidade() { System.out.println("Mais rápido com baixa sanidade."); }
}

class Deogen extends Fantasma {
    public Deogen() {
        super("Deogen", Evidencia.SPIRIT_BOX, Evidencia.GHOST_WRITING, Evidencia.DOTS);
    }
    public void habilidade() { System.out.println("Sempre encontra jogador."); }
}

class Thaye extends Fantasma {
    public Thaye() {
        super("Thaye", Evidencia.ORB, Evidencia.GHOST_WRITING, Evidencia.DOTS);
    }
    public void habilidade() { System.out.println("Envelhece e enfraquece."); }
}
public class Phasmophobia {

    public static void main(String[] args) {

        List<Fantasma> fantasmas = List.of(
            new Spirit(), new Wraith(), new Phantom(), new Poltergeist(),
            new Banshee(), new Jinn(), new Mare(), new Revenant(),
            new Shade(), new Demon(), new Yurei(), new Oni(),
            new Yokai(), new Hantu(), new Goryo(), new Myling(),
            new Onryo(), new TheTwins(), new Raiju(), new Obake(),
            new Mimic(), new Moroi(), new Deogen(), new Thaye()
        );

        // Simulação: jogador encontrou evidências
        Set<Evidencia> evidenciasEncontradas = new HashSet<>();
        evidenciasEncontradas.add(Evidencia.SPIRIT_BOX);
        evidenciasEncontradas.add(Evidencia.GHOST_WRITING);

        System.out.println("Possíveis fantasmas:\n");

        for (Fantasma f : fantasmas) {
            if (f.combinaCom(evidenciasEncontradas)) {
                System.out.println("- " + f.getNome());
            }
        }
    }
}