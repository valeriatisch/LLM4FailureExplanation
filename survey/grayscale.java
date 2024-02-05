package org.jfree.chart.renderer;

import java.awt.Color;
import java.awt.Paint;
import java.io.Serializable;

import org.jfree.chart.util.PublicCloneable;

/**
 * A paint scale that returns shades of gray.
 * 
 * @since 1.0.4
 */
public class GrayPaintScale 
        implements PaintScale, PublicCloneable, Serializable {

    /** The lower bound. */
    private double lowerBound;
    
    /** The upper bound. */
    private double upperBound;
    
    /**
     * Creates a new <code>GrayPaintScale</code> instance with default values.
     */
    public GrayPaintScale() {
        this(0.0, 1.0);
    }
    
    /**
     * Creates a new paint scale for values in the specified range.
     * 
     * @param lowerBound  the lower bound.
     * @param upperBound  the upper bound.
     */
    public GrayPaintScale(double lowerBound, double upperBound) {
        if (lowerBound >= upperBound) {
            throw new IllegalArgumentException(
                    "Requires lowerBound < upperBound.");
        }
        this.lowerBound = lowerBound;
        this.upperBound = upperBound;
    }
    
    /**
     * Returns the lower bound.
     * 
     * @return The lower bound.
     */
    public double getLowerBound() {
        return this.lowerBound;
    }

    /**
     * Returns the upper bound.
     * 
     * @return The upper bound.
     */
    public double getUpperBound() {
        return this.upperBound;
    }

    /**
     * Returns a paint for the specified value.
     * 
     * @param value  the value.
     * 
     * @return A paint for the specified value.
     */
    public Paint getPaint(double value) {
        double v = Math.max(value, this.lowerBound);
        v = Math.min(v, this.upperBound);
        int g = (int) ((value - this.lowerBound) / (this.upperBound 
                - this.lowerBound) * 255.0);
        return new Color(g, g, g);
    }
    
    /**
     * Tests this <code>GrayPaintScale</code> instance for equality with an
     * arbitrary object.  This method returns <code>true</code> if and only
     * if:
     * <ul>
     * <li><code>obj</code> is not <code>null</code>;</li>
     * <li><code>obj</code> is an instance of <code>GrayPaintScale</code>;</li>
     * </ul>
     * 
     * @param obj  the object (<code>null</code> permitted).
     * 
     * @return A boolean.
     */
    public boolean equals(Object obj) {
        if (obj == this) {
            return true;
        }
        if (!(obj instanceof GrayPaintScale)) {
            return false;
        }
        GrayPaintScale that = (GrayPaintScale) obj;
        if (this.lowerBound != that.lowerBound) {
            return false;
        }
        if (this.upperBound != that.upperBound) {
            return false;
        }
        return true;    
    }
    
    /**
     * Returns a clone of this <code>GrayPaintScale</code> instance.
     * 
     * @return A clone.
     * 
     * @throws CloneNotSupportedException if there is a problem cloning this
     *     instance.
     */
    public Object clone() throws CloneNotSupportedException {
        return super.clone();
    }
    
}
